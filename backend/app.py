from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# Load env variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ OPENAI_API_KEY not found. Please set it in .env")

# Initialize LangChain LLM wrapper
llm = ChatOpenAI(
    model="gpt-3.5-turbo",   # you can switch to gpt-4o-mini later
    temperature=0.7,         # higher = more creative, lower = more focused
    api_key=OPENAI_API_KEY   # securely loaded from .env
)


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running from app.py!"}

@app.get("/plan")
def get_plan(goal: str):
    return {"plan": f"Here is a sample workout plan for {goal}"}





@app.get("/test_ai")
def test_ai():
    response = llm.invoke("Give me a quick 3-day beginner workout plan.")
    return {"ai_response": response.content}



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


