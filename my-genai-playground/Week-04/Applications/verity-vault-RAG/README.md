---
title: VerityVault AI
emoji: 🐢
colorFrom: pink
colorTo: yellow
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
license: mit
short_description: Grounded document intelligence with zero hallucinations.
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference



# 🛡️ VerityVault AI: Professional RAG Intelligence

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![LLM](https://img.shields.io/badge/LLM-Llama%203.3-blueviolet)

**"Grounded document intelligence with zero hallucinations."**

---

## 🌟 Introduction (What is VerityVault?)
**VerityVault AI** is a sophisticated **Retrieval-Augmented Generation (RAG)** application designed for users who need absolute factual accuracy. In an era where AI often "hallucinates" (makes up facts), VerityVault acts as a **Strict Librarian**. It locks the AI's knowledge to *only* the documents you provide, ensuring every answer is backed by your own data.

## 🚀 How It Works 

VerityVault doesn't just read your file; it understands the structure through a multi-stage pipeline:

1.  **Ingestion:** The system loads PDF or TXT files using specialized loaders.
2.  **Chunking:** Large documents are broken into 800-character "intelligent chunks" to maintain context.
3.  **Embedding:** Each chunk is converted into a high-dimensional vector using the `BGE-Small-En` model.
4.  **Vector Vault:** These vectors are stored in a **FAISS** (Facebook AI Similarity Search) database for lightning-fast retrieval.
5.  **Strict Retrieval:** When you ask a question, the system finds the top 3 most relevant chunks and feeds them to the LLM.
6.  **Grounded Generation:** The **Llama 3.3** model (via Groq) generates a professional response *only* using those chunks.

## 🛠️ How It Was Built 

This project was engineered using the latest 2026 AI standards:

* **Brain (LLM):** `Meta Llama-3.3-70b-versatile` via **Groq Cloud** for sub-second inference speeds.
* **Orchestration:** **LangChain** (Classic & Community) for managing the RAG pipeline.
* **Vector Database:** **FAISS-CPU** for efficient local similarity searching.
* **Embeddings:** `BAAI/bge-small-en-v1.5` – a state-of-the-art embedding model from Hugging Face.
* **Frontend:** **Gradio** – designed with a premium "Glassmorphism" theme and responsive UI.

## 📂 Installation & Deployment

To run this project locally:

1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/verity-vault-rag.git](https://github.com/YOUR_USERNAME/verity-vault-rag.git)
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Environment Setup:**
    Add your Groq API Key to your environment variables as `MY_GROQ_KEY`.
4.  **Run Application:**
    ```bash
    python app.py
    ```

---

## 👨‍💻 Developed By

**Bilal** *AI Developer & RAG Engineer*

---

## 🔗 Connect & Explore
I am passionate about building grounded AI solutions. Feel free to reach out or test the live application!

* **🌐 Live Demo (Hugging Face):** https://huggingface.co/spaces/bkbilal09/VerityVault-AI
* **👔 LinkedIn:** : https://www.linkedin.com/in/muhammad-bilal-dev/
* **🐙 GitHub Repo:** : https://github.com/bkbilal009/verity-vault-rag/tree/main

---
*License: MIT. Developed for educational and research purposes in document intelligence.*
