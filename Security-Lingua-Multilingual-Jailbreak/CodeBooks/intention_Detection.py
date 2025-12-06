import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

# -----------------------------
# Load input CSV
# -----------------------------
df = pd.read_csv("multijail.csv")   # change filename if needed

languages = ["en", "zh", "it", "vi", "ar", "ko", "th", "bn", "sw", "jv"]

# -----------------------------
# Load SecurityLingua model
# -----------------------------
model_name = "SecurityLingua/securitylingua-xlm-s2s"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# -----------------------------
# List to collect all results
# -----------------------------
results = []

# -----------------------------
# Loop over rows and languages
# -----------------------------
for idx, row in df.iterrows():

    for lang in languages:
        text = row[lang]

        # --- Tokenize ---
        inputs = tokenizer(text, return_tensors="pt", truncation=True)

        # --- Run inference ---
        with torch.no_grad():
            outputs = model(**inputs)

        logits = outputs.logits
        predictions = torch.argmax(logits, dim=-1).squeeze().tolist()

        # --- Get selected tokens ---
        tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"].squeeze())
        selected_tokens = [
            tok for tok, label in zip(tokens, predictions) if label == 1
        ]
        compressed_text = tokenizer.convert_tokens_to_string(selected_tokens)
        # -----------------------------
        # Save into results buffer
        # -----------------------------
        results.append({
            "id": row["id"],
            "language": lang,
            "original_text": text,
            "compressed_tokens": " ".join(selected_tokens),
            "compressed_text": compressed_text
        })

# -----------------------------
# Save final output CSV
# -----------------------------
output_df = pd.DataFrame(results)
output_df.to_csv("intentions.csv", index=False)

print("Saved output to intentions.csv")
