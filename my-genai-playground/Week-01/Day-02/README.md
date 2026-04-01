# 🚀 Day 02 - Understanding and Using APIs

## 📌 Overview

Today’s focus was to understand **APIs**, how they work, and how to **create and securely store API keys** for using AI models and services.

---

## 🧠 Topics Covered

### 🔹 What is an API?

API (Application Programming Interface) is a system that allows different software applications to communicate with each other.

### 💡 Simple Idea:

* You send a request
* The API processes it
* You receive a response

---

### 🔹 How APIs Work

1. Client sends a request (e.g., a prompt)
2. Server processes the request
3. Server returns a response (e.g., generated text)

---

### 🔹 Using APIs

* APIs are used to interact with services like AI models
* You send input (prompt/data) and receive output (response)

#### Example Use Cases:

* Chatbots
* Image generation
* Data processing
* Integration with apps/websites

---

## 🔐 API Keys

### 🔹 What is an API Key?

* A unique secret key used to authenticate and access an API
* Works like a password for your application

---

### 🔹 Creating an API Key

1. Sign up on the platform (e.g., OpenAI)
2. Go to API settings/dashboard
3. Generate a new API key
4. Copy and store it safely

---

### 🔹 Securely Storing API Keys (VERY IMPORTANT 🔥)

#### ❌ What NOT to do:

* Do not hardcode API keys in source code
* Do not upload keys to GitHub
* Do not share keys publicly

---

#### ✅ Best Practices:

* Use environment variables (.env file)
* Store keys in secure vaults
* Restrict API key permissions
* Rotate keys regularly

---

### 🔹 Example (.env file)

```env
API_KEY=your_secret_key_here
```

---

## 🎯 Key Learnings

* APIs enable communication between applications
* API keys are essential for authentication
* Security of API keys is critical
* Best practices prevent misuse and data leaks

---

## 📅 Progress

✅ Day 02 Completed
📘 Focus: APIs & Security Basics

