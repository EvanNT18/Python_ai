import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


from PyPDF2 import PdfReader

def load_pdf_text(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def summarize_pdf(pdf_path: str, language: str = "Bahasa Indonesia") -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=api_key)

    raw_text = load_pdf_text(pdf_path)

    prompt_template = PromptTemplate(
        input_variables=["context", "language"],
        template="""
        Anda adalah asisten AI yang cerdas. Tugas Anda adalah merangkum teks berikut dalam {language} secara ringkas, jelas, dan informatif:

        ---TEKS---
        {context}
        """
    )

    llm_chain = LLMChain(llm=llm, prompt=prompt_template)

    result = llm_chain.run({"context": raw_text, "language": language})
    return result

