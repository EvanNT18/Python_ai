import os
from dotenv import load_dotenv
from fastapi import FastAPI
from typing import TypedDict
from pydantic import BaseModel
from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

app = FastAPI()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

class GreetState(TypedDict):
    name: str
    result: str

def greet_node(state: GreetState) -> GreetState:
    prompt = f"Buatkan satu sapaan ramah dan singkat untuk seseorang bernama {state['name']}."
    response = llm.invoke(prompt)
    content = response.content if hasattr(response, "content") else str(response)
    
    return {
        "result": content.strip()
    }

builder = StateGraph(GreetState)
builder.add_node("greet", greet_node)
builder.set_entry_point("greet")
graph = builder.compile()

class GreetRequest(BaseModel):
    name: str

@app.post("/greet")
def greet(request: GreetRequest):
    result = graph.invoke({"name": request.name})
    return {"result": result["result"]}

