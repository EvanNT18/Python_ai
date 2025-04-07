# 🚀 LangGraph Greeting API

## 🔧 How to Run

```bash
# 1. Clone repo (opsional kalau belum punya)
git clone https://github.com/username/langgraph-greeting-api.git
cd langgraph-greeting-api

# 2. Buat dan aktifkan virtual environment
python -m venv venv
venv\Scripts\activate         # Windows
# atau
source venv/bin/activate      # Linux/Mac

# 3. Install semua dependencies
pip install -r requirements.txt

# 4. Buat file .env di root folder, isi dengan:
# (ganti your_google_api_key dengan API key milikmu)
echo GEMINI_API_KEY=your_google_api_key > .env

# 5. Jalankan server FastAPI
uvicorn main:app --reload

# 6. Buka di browser:
# Swagger UI: http://localhost:8000/docs
# Endpoint: POST /greet dengan JSON body: { "name": "Evan" }
```
