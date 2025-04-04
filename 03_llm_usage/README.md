# 🎥 YouTube Summarizer API with Gemini

Project ini adalah API sederhana untuk **menyimpulkan video YouTube** menggunakan **transkrip video dan Google Gemini API**. Dibuat dengan **FastAPI** dan cocok buat eksplorasi LLM (Large Language Model).

---

## 🚀 Fitur

- Ekstraksi transkrip dari video YouTube (otomatis)
- Summarization menggunakan Gemini (Google Generative AI)
- Endpoint API untuk konsumsi data via frontend atau tools seperti Postman

---

## 🧠 Prompt Engineering

Prompt yang digunakan:

> “Summarize the following YouTube transcript in a clear and concise way”

Ditambah sistem instruksi seperti:

> "You are an AI specialized in summarizing YouTube video transcripts clearly and accurately."

---

## 🛠️ Cara Instalasi

1. Clone repo ini atau copy ke lokal
2. Buat dan aktifkan virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```
