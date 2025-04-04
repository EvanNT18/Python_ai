# 🎥 YouTube Summarizer API with Gemini

Project ini adalah API sederhana untuk **menyimpulkan video YouTube** menggunakan **transkrip video** dan **Google Gemini API**, dibuat dengan **FastAPI**.

---

## 🚀 Fitur

- ✅ Ekstraksi transkrip dari video YouTube secara otomatis
- ✅ Summarization menggunakan Gemini (Google Generative AI)
- ✅ Endpoint API bisa diakses via frontend atau tools seperti Postman

---

## ▶️ Cara Menjalankan

1. **Clone / download project**
2. **Buat virtual environment** dan aktifkan:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   ```
3. **Install dependency:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Buat file `.env` dan isi:**
   ```env
   GEMINI_API_KEY=masukkan_api_key_anda
   ```
5. **Jalankan server:**
   ```bash
   uvicorn main:app --reload
   ```
6. **Akses endpoint:**
   ```
   http://localhost:8000/summarize?url=https://youtu.be/VIDEO_ID
   ```

---
