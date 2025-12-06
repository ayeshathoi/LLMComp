from datasets import load_dataset

ds = load_dataset("JailbreakBench/JBB-Behaviors", "judge_comparison")

df = ds["test"].to_pandas()
df.to_csv("judge_comparison_test.csv", index=False)

print("Saved judge_comparison_test.csv")
