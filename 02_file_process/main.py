from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import fitz
import io
import re
import tempfile

app = FastAPI()

async def extract_text_from_pdf(pdf_file: UploadFile) -> str:

    try:
        
        pdf_bytes = await pdf_file.read()
        doc = fitz.open(stream=io.BytesIO(pdf_bytes), filetype="pdf")

        text = ""
        for page in doc:
           
            extracted = page.get_text("text")
            if not extracted.strip():
                blocks = page.get_text("blocks")
                extracted = " ".join([b[4] for b in blocks if len(b) > 4])

            text += extracted + "\n"

        
        cleaned_text = clean_text(text)
        return cleaned_text if cleaned_text.strip() else "Error: PDF tidak mengandung teks yang bisa diekstrak."

    except Exception as e:
        return f"Error: {str(e)}"

def clean_text(text: str) -> str:
   
    text = re.sub(r'\s+', ' ', text)  
    text = text.replace("\xa0", " ")  
    return text.strip()

def convert_text_to_markdown(text: str) -> str:
  
    paragraphs = text.split("\n")
    md_text = "# Extracted Text\n\n"
    for p in paragraphs:
        p = p.strip()
        if len(p) > 50:  
            md_text += f"\n{p}"
        elif p:  
            md_text += f"\n## {p}"

    return md_text

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
  
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File harus berformat PDF")

    try:
        
        extracted_text = await extract_text_from_pdf(file)
        if extracted_text.startswith("Error"):
            raise HTTPException(status_code=400, detail=extracted_text)

        
        markdown_text = convert_text_to_markdown(extracted_text)

        
        md_file = file.filename.replace('.pdf', '.md')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.md') as temp_file:
            temp_file.write(markdown_text.encode('utf-8'))
            temp_file.close()

            
            return FileResponse(
                path=temp_file.name,
                media_type="text/markdown",
                filename=md_file
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
