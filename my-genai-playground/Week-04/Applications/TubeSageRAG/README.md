---
title: TubeSage-RAG-Engine
emoji: 📺
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
license: mit
short_description: Advanced AI engine to chat with any YouTube video context
---

# 📺 TubeSage RAG: High-Performance Video Intelligence

> **"Video watching is passive, Video chatting is active."**
> TubeSage RAG ek advanced conversational engine hai jo YouTube videos ko searchable knowledge bases mein convert karta hai. Developed by **Muhammad Bilal**.

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-Llama_3.3_70B-f34f29?style=for-the-badge)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-04A1E6?style=for-the-badge)

---

## 🏛️ Project Vision
YouTube par ghanton lambi tutorials aur podcasts dekhna mushkil kaam hai. **TubeSage RAG** ko **Muhammad Bilal** ne isliye engineer kiya hai taake aap sirf 10 seconds mein kisi bhi video ka "Dimagh" (Context) capture kar saken. Ye system transcript fetch karta hai, usay analyze karta hai, aur aapke sawalon ke jawab directly video ke context se deta hai.

---

## 🏗️ Technical Architecture (Under the Hood)

Is project ka backbone modern **RAG (Retrieval-Augmented Generation)** pipeline par mushtamil hai:

### 1. Advanced Extraction (The Bridge)
* **Transcript API:** `youtube-transcript-api` ka istemal kar ke raw data nikala jata hai.
* **Cookie Bypass:** Request blocking se bachne ke liye session cookies integrate ki gayi hain, jo system ki reliability ko 100% banati hain.

### 2. Knowledge Structuring (The Brain)
* **Recursive Character Splitting:** Text ko 1000 characters ke chunks mein break kiya jata hai taake context lose na ho.
* **High-Dimensional Embeddings:** `all-MiniLM-L6-v2` transformers ke zariye text ko mathematical vectors mein convert kiya jata hai.
* **FAISS Vector Store:** In vectors ko index kiya jata hai taake similarity search lightning-fast ho.

### 3. Intelligent Reasoning (The LLM)
* **Inference Engine:** Groq Cloud ka istemal kiya gaya hai jo **Llama 3.3 70B** model ko industry-leading speed par chalata hai.
* **Semantic Retrieval:** User ka sawal aate hi system sabse relevant 3 chunks uthata hai aur LLM ko bhejta hai.

---

## 🛠️ Tech Stack (The Muhammad Bilal Signature)

| Component | Technology | Professional Impact |
| :--- | :--- | :--- |
| **Language Model** | Llama 3.3 70B (Groq) | Human-like Reasoning |
| **Framework** | LangChain (LCEL) | Modular & Scalable Code |
| **Vector Engine** | FAISS | Millisecond Retrieval |
| **Embeddings** | HuggingFace Transformers | Semantic Understanding |
| **Frontend UI** | Gradio (Indigo & Violet Theme) | Modern Glass-morphism UX |

---

## 🚀 Key Features
* **Zero-Buffer Analysis:** YouTube videos ko seconds mein process karna.
* **Contextual Integrity:** AI sirf video ke content tak mehdood rehta hai (No Hallucinations).
* **Bypass Technology:** Automated bots detection ko bypass karne ke liye unique cookie-handling logic.
* **Professional UI:** Developed specifically for high-end portfolio presentation.

---

## 👨‍💻 Developer Profile
**Muhammad Bilal**
*Aspiring AI Developer | Technical Professional | Competitive Programmer (LeetCode 144+).*
Participant in HEC Pakistan Generative AI Training Program. Specialized in building grounded AI systems that solve real-world data problems.

### 🌐 Connect & Collaborate:
| Platform | Link |
| :--- | :--- |
| **GitHub** | [📂 My Portfolio](https://github.com/bkbilal009) |
| **LinkedIn** | [💼 Professional Network](https://www.linkedin.com/in/muhammad-bilal-dev/) |
| **Hugging Face** | [🚀 Live Project Demo](https://huggingface.co/spaces/bkbilal09/TubeSage) |

---
*Intelligence. Efficiency. Accuracy.*
