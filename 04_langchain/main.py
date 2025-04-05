from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
import tempfile
from app.summarizer import summarize_pdf
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

@app.post("/summarize-pdf")
async def summarize_pdf_endpoint(
    file: UploadFile = File(...),
    language: str = Form("Bahasa Indonesia")  
):
    try:
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            contents = await file.read()
            tmp.write(contents)
            tmp_path = tmp.name

        
        summary = summarize_pdf(tmp_path, language)

        
        os.remove(tmp_path)

        return {"summary": summary}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
