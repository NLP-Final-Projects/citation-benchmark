<div align="center">

# 📚 Citation Benchmark

### *A Comprehensive Framework for Evaluating Citation Quality in Generative Language Models*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Sharif University](https://img.shields.io/badge/Sharif-University%20of%20Technology-purple.svg)](https://www.sharif.edu/)

</div>

---

## 🌟 Overview

**Citation Benchmark** is a research project that proposes a comprehensive framework for evaluating how well large language models (LLMs) generate and utilize reference citations. The system introduces novel metrics and automated pipelines to assess the factual accuracy and attribution quality of LLM-generated text — minimizing the need for costly and subjective human judgment.

> 📄 This project was developed as part of the **NLP Final Project** at the **Computer Engineering Department, Sharif University of Technology, Tehran**.

---

## 🎯 Key Objectives

- ✅ Establish a **standardized benchmark procedure** for evaluating citation quality across different LLMs
- 📏 Introduce **novel automated metrics** that leverage correlation-based assessments of sentence fragments within documents
- ⚡ Optimize **input processing** by reducing token count through relevant snippets, summaries, and named-entity-based document reconstruction
- 🏗️ Develop **structured input formats** that improve consistency and accuracy of model outputs
- 🔍 Propose a **new citation evaluation metric** compatible with Perplexity.AI and Microsoft Copilot models

---

## 🧠 Methodology

The framework follows a multi-stage pipeline:

### 1️⃣ Citation Extraction
Extract cited sentences along with their reference URLs from LLM responses. Supports multiple formats:
- **Perplexity.AI** — Bracketed citation numbers (e.g., `[1][2]`)
- **Microsoft Copilot** — UTF-8 superscript-based citation markers

### 2️⃣ Atomic Fact Decomposition
Each cited passage is decomposed into independent, self-contained **atomic facts** using a referee LLM (GPT-4o Mini). This ensures fine-grained verification at the statement level.

### 3️⃣ Reference Content Retrieval
Citation URLs are scraped to extract the visible text content of the referenced web pages using a custom `Webscraper` class built with `BeautifulSoup`.

### 4️⃣ Fact Verification
Each atomic fact is verified against its cited reference content using LLM-based entailment checks. A binary vector is produced for each set of facts:
- `1` → Fact is **supported** by the cited reference
- `0` → Fact is **not supported** by the cited reference

### 5️⃣ Scoring & Evaluation
Standard metrics including **Citation Recall**, **Citation Precision**, **ROUGE-L**, **STR-EM**, and **QA-based accuracy** are computed using the ALCE evaluation framework, enhanced with an NLI-based AutoAIS model (`google/t5_xxl_true_nli_mixture`).

---

## 🏗️ Architecture

The main pipeline (`MainPipeline.ipynb`) is structured into four core components:

| Component | Description |
|-----------|-------------|
| **🔧 Utils** | Text normalization, citation removal, GPU memory management, prompt formatting, and model loading utilities |
| **🔎 Searcher** | Within-document retrieval using TF-IDF or GTR dense retrieval (`sentence-transformers/gtr-t5-large`) |
| **🚀 Run** | End-to-end inference pipeline supporting OpenAI API, Azure, and local HuggingFace models (OPT, LLaMA, Vicuna) with ICL demonstrations |
| **📊 Eval** | Comprehensive evaluation including ROUGE, STR-EM, QA-F1, Citation Recall/Precision, and MAUVE scores |

---

## 📂 Repository Structure

```
citation-benchmark/
├── 📓 MainPipeline.ipynb        # Main inference & evaluation pipeline (ALCE-based)
├── 📓 Metric.ipynb              # Novel citation metric pipeline (Perplexity/Copilot)
├── 📁 query_llms/               # Utility scripts for querying LLMs via Poe API
│   ├── poe-api.py               # Basic async Poe API wrapper example
│   └── poe_api_wrapper.ipynb    # Notebook for LLM querying via poe-api-wrapper
├── 📁 Report/                   # LaTeX source for the academic report
│   ├── paper.tex                # Main LaTeX document
│   ├── paper.bib                # Bibliography references
│   ├── sections/                # Report sections (abstract, intro, related work, etc.)
│   └── Makefile                 # Build system for the report PDF
├── 📄 LICENSE                   # MIT License
└── 📄 README.md                 # This file
```

---

## 📊 Datasets

The framework is validated using the following diverse datasets:

| Dataset | Description |
|---------|-------------|
| **ASQA** | Ambiguous factoid questions requiring long-form answers with citations |
| **QAMPARI** | Questions with multiple entity answers |
| **ELI5** | Open-ended "Explain Like I'm 5" questions |
| **Wikidata5m** | Knowledge graph-based attribution evaluation |

---

## 🤖 Supported Models

| Model | Type |
|-------|------|
| **GPT-3.5 Turbo / GPT-4** | OpenAI API |
| **LLaMA 2 / LLaMA 3 (8B)** | Local (HuggingFace) |
| **OPT-6.7B** | Local (HuggingFace) |
| **Vicuna** | Local (HuggingFace) |
| **GPT-4o Mini** | Via Poe API (for referee tasks) |
| **Perplexity.AI / Copilot** | Evaluated as target systems |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- CUDA-compatible GPU (recommended: ≥16GB VRAM)
- [Hugging Face](https://huggingface.co/) account (for gated models like LLaMA)

### Installation

```bash
# Clone the repository
git clone https://github.com/NLP-Final-Projects/citation-benchmark.git
cd citation-benchmark

# Install dependencies
pip install torch transformers spacy scikit-learn rouge-score nltk openai poe-api-wrapper beautifulsoup4 requests bitsandbytes safetensors

# Download spaCy model
python -m spacy download en_core_web_sm

# Download ALCE dataset
wget https://huggingface.co/datasets/princeton-nlp/ALCE-data/resolve/main/ALCE-data.tar
tar xvf ALCE-data.tar && mv ALCE-data data && rm ALCE-data.tar
```

### Running the Main Pipeline

Open `MainPipeline.ipynb` in Jupyter or Google Colab and follow the step-by-step cells for:
1. Data preparation & document summarization
2. Prompt generation with ICL demonstrations
3. Model inference
4. Comprehensive evaluation

### Running the Citation Metric

Open `Metric.ipynb` to run the novel citation evaluation pipeline:
1. Extract citations from LLM responses (Perplexity.AI / Copilot format)
2. Decompose into atomic facts
3. Scrape reference web pages
4. Verify facts against references
5. Compute citation accuracy scores

---

## 📈 Key Results

Using the ASQA dataset with OPT-6.7B (1-shot, 3 documents):

| Metric | Score |
|--------|-------|
| **STR-EM** | 22.33 |
| **STR-HIT** | 8.00 |
| **ROUGE-Lsum** | 29.92 |
| **Citation Recall** | 4.20 |
| **Citation Precision** | 5.67 |
| **Avg. Output Length** | 87.7 words |

> 💡 A novel contribution is the use of **named entity extraction + LLaMA 3** for document reconstruction (instead of traditional summarization), which achieved higher reference-finding metrics.

---

## 👥 Authors

| Name | Email |
|------|-------|
| **Ilia Hashemi Rad** | iliahashemirad@gmail.com |
| **Ali Nazari** | ali.nazari.8102@gmail.com |
| **Shayan Salehi** | s.salehi1381@gmail.com |
| **Seyed Mohammad Yousef Najafi** | najafim2002@gmail.com |
| **Amir Mohammad Fakhimi** | fakhimi.amirmohamad@gmail.com |

---

## 📝 Citation

If you use this work in your research, please cite:

```bibtex
@misc{citation-benchmark2024,
  title={Citation Benchmark: A Framework for Evaluating Citation Quality in Generative Language Models},
  author={Hashemi Rad, Ilia and Nazari, Ali and Salehi, Shayan and Najafi, Seyed Mohammad Yousef and Fakhimi, Amir Mohammad},
  year={2024},
  institution={Sharif University of Technology}
}
```

---

## 🙏 Acknowledgements

- [ALCE](https://github.com/princeton-nlp/ALCE) — Enabling LLMs to Generate Text with Citations (Princeton NLP)
- [poe-api-wrapper](https://github.com/snowby666/poe-api-wrapper) — Python library for querying LLMs via Poe
- [Hugging Face](https://huggingface.co/) — Model hosting and datasets
- Sharif University of Technology — Academic support

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

</div>
