# LLMComp: Prompt Compression for Robust Defense Against LLM Jailbreaks

This repository presents **LLMComp**, a prompt-compression–based defense mechanism designed to improve robustness against Large Language Model (LLM) jailbreak attacks in both monolingual and multilingual settings. This work is built upon and extends **SecurityLingua** (Li et al.), which is adopted as a baseline defense mechanism and further evaluated in multilingual jailbreak scenarios.

This project was created by Debrup Das, Ayesha Binte Mostofa, and Abhranil Chandra as a course project for COMPSCI 660 in Fall 2025.

---

## Overview

Large Language Models remain susceptible to jailbreak attacks that conceal malicious intent within verbose, obfuscated, or multilingual prompts. Existing defense mechanisms face inherent trade-offs between **security robustness**, **utility preservation**, **latency**, and **deployment cost**, motivating the need for efficient and scalable **intention extraction** methods.

This project systematically investigates:

- SecurityLingua as a token-classification–based compressor  
- LLM-based generative compressors (LLMComp) using Qwen-2.5 models  
- Zero-shot and few-shot intention extraction strategies  
- Robustness evaluation on multilingual jailbreak prompts  

---

## Key Contributions

### 1. Multilingual Evaluation of SecurityLingua
- Adopted **SecurityLingua** (Li et al.) as the core baseline defense model
- Applied it to multilingual prompts from **MultiJail** covering 10 languages
- Conducted both **zero-shot** and **3-shot** intention-guided defense experiments
- Evaluated defense effectiveness and over-conservativeness in multilingual settings

### 2. LLM-Based Prompt Compression (LLMComp)
- Investigated generative intention extraction using **Qwen-2.5 (3B / 7B)** models
- Compared **zero-shot versus few-shot compression strategies**
- Benchmarked downstream defense performance against SecurityLingua and baseline LLMs

### 3. Multilingual Dataset Construction
- Constructed a **3,000-sample multilingual dataset** from JailbreakBench (benign and harmful prompts)
- Translated samples into **10 languages** following the MultiJail methodology
- Dataset is currently used for **supervised finetuning** of LLM-based compressors

---

## Ongoing Work

- Finetuning **Qwen-2.5-3B-Instruct** and **Qwen-2.5-7B-Instruct** on the constructed multilingual dataset
- Evaluating whether trained LLM-based compressors can surpass SecurityLingua in both:
  - Multilingual robustness
  - Utility preservation on benign prompts

---


## Methodology

### SecurityLingua (Baseline Defense)

SecurityLingua is adopted directly from the original work by **Yucheng Li et al.** as a baseline defense mechanism.

- Architecture: Transformer encoder with a linear classification head  
- Task: Token-level binary decision (preserve or discard)  
- Output: A compressed sequence representing the core intent of the prompt  

### LLMComp (Generative Compressor)

- Performs direct **generative intention extraction**
- Uses **short-output constraints** to enforce compression
- Prompts include either:
  - Zero-shot guidance
  - Few-shot guidance
- The final system prompt provided to the target LLM includes:
  - The extracted compressed intention
  - The original user prompt (unchanged)

---

## Evaluation Metrics

- **Harmful Prompts:** Rejection Rate (higher is better)  
- **Benign Prompts:** Answer Rate (higher is better)  
- Refusal behavior is detected via **keyword-based proxy signals**

---

## Datasets

- **JailbreakV-28K**
- **JailbreakBench Behaviors** (benign and harmful)
- **MultiJail**
- **Synthetic Multilingual Dataset (Ours)** – 10 languages, 3,000 samples

---

## Results (Summary)

- SecurityLingua demonstrates strong defense performance but exhibits **over-conservativeness**, which reduces benign utility.
- LLMComp shows **competitive performance**, particularly under **few-shot prompting**, though it currently trails SecurityLingua before finetuning.
- **Multilingual jailbreaks significantly increase attack success rates**, highlighting the importance of multilingual training.
- Few-shot prompting **consistently improves robustness** across models.
- Ongoing finetuning is expected to **close the performance gap** between LLMComp and SecurityLingua while improving multilingual generalization.

---

## Citation and Acknowledgment

This work **adopts and extends SecurityLingua**. If you use SecurityLingua-related components, please cite the original paper:

> Yucheng Li et al. SecurityLingua: Efficient Defense of LLM Jailbreak Attacks via Secure Prompt Compression. 2024.


---

## Resources

- [Project Report](https://github.com/ayeshathoi/LLMComp/blob/main/Resources/LLMComp-COMPSCI660-Report.pdf)
- [Project Presentation Slide](https://github.com/ayeshathoi/LLMComp/blob/main/Resources/LLMComp-CS660-Project.pdf)
- [Project Proposal](https://github.com/ayeshathoi/LLMComp/blob/main/Resources/Proposal%20Proposal.pdf)
