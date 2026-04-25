---
title: DocuVortex
emoji: ⚡
colorFrom: red
colorTo: green
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
license: mit
short_description: Strict AI grounded in private documents
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference



# 🌀 Vortex-RAG: Extreme-Precision Intelligence Engine

> **Engineering reliable AI through strict-grounding protocols.**
> 

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-f34f29?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/Deployed-HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

---

## 🏛️ Project Vision

Standard Large Language Models (LLMs) suffer from **stochastic hallucinations**—they prioritize being helpful over being truthful. **Vortex-RAG** is engineered to solve this. It is a "Zero-Trust" AI system that treats external data as the only source of truth.

Developed by **Muhammad Bilal**, this project demonstrates the bridge between high-speed inference and high-accuracy retrieval.

---

## 🏗️ Technical Architecture

Vortex-RAG follows a sophisticated pipeline to ensure that every word generated is backed by data.



### 1. The Ingestion Layer

* **Dynamic Stream:** Securely fetches documents from encrypted cloud storage.
* **Smart Chunking:** Utilizes `RecursiveCharacterTextSplitter` with an 800-token window and 150-token overlap to maintain semantic context across chunks.

### 2. The Vector Brain

* **Embeddings:** Powered by `sentence-transformers/all-MiniLM-L6-v2`, mapping text into a 384-dimensional dense vector space.
* **Indexing:** **FAISS** (Facebook AI Similarity Search) provides sub-millisecond retrieval of context, even in massive datasets.

### 3. The Strict Inference Protocol

* **Hardware:** Running on Groq's LPU (Language Processing Unit) for near-instant response times.
* **System Prompting:** A proprietary prompt structure forces the Llama 3.3 model into a "Reference-Only" mode. 

---

## 🛠️ Performance Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Model** | Llama 3.3 70B (Versatile) | Reasoning & Response |
| **Inference** | Groq Cloud | Hardware Acceleration |
| **Orchestration**| LangChain | Pipeline Management |
| **Database** | FAISS | Vector Similarity Search |
| **Interface** | Gradio (Glass Theme) | Professional UI/UX |

---

## 🔐 Privacy & Security Features

* **In-Memory Logic:** Documents are converted to vectors and the original files are purged from the server instantly.
* **Stateless API:** No user chat history is stored on the server, ensuring total confidentiality for research data.

---

## 🚀 Deployment Guide

To replicate this environment on Hugging Face:
1. **Repository:** Create a new Space using the Gradio SDK.
2. **Secrets:** Add `MY_GROQ_SECRET` in the settings tab.
3. **Trigger:** The `app.py` will automatically run the startup indexing script.

---

## 👨‍💻 Developer Profile

**Muhammad Bilal** *Aspiring AI Developer & Data Structures Specialist* Focusing on the intersection of Machine Learning and Scalable Software Architecture. 

### 🌐 Connect with my Journey
| Platform | Link |
| :--- | :--- |
| **GitHub** | [📂 View My Repositories](https://github.com/bkbilal009/Vortex-RAG) |
| **LinkedIn** | [💼 Professional Network]([YOUR_LINK_HERE](https://www.linkedin.com/in/muhammad-bilal-dev/)) |
| **Hugging Face** | [🚀 Live Demo]([YOUR_LINK_HERE](https://huggingface.co/spaces/bkbilal09/DocuVortex/tree/main)) |

---
*Created with a focus on precision, speed, and integrity.*
