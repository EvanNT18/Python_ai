import os
import dotenv
import google.generativeai as genai

dotenv.load_dotenv()

def summarize_with_gemini(context: str) -> str:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    
    model = genai.GenerativeModel("gemini-1.5-pro")  

    prompt = (
    "You are an expert at summarizing YouTube video transcripts. "
    "Generate a short, clear, and informative summary from the transcript below.\n\n"
    f"Transcript:\n{context}"
)


    
    response = model.generate_content(prompt)
    return response.text
