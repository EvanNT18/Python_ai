# 📄 PDF Summarizer API

API untuk merangkum file PDF menggunakan LangChain + Gemini Pro.

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install fastapi uvicorn python-multipart PyPDF2 langchain langchain-google-genai python-dotenv
```

### 2. Buat file `.env`

```env
GEMINI_API_KEY=your_google_api_key_here
```

### 3. Jalankan server

```bash
uvicorn main:app --reload
```

### 4. Akses endpoint via Postman

**POST** `http://localhost:8000/summarize`  
**Form-data**:

- `file`: Upload file PDF
- `language`: Bahasa ringkasan (contoh: `Bahasa Indonesia`)

---

📌 Done!
