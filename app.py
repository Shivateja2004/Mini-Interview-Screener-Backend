from groq import Groq
from dotenv import load_dotenv
import os, json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("MODEL", "llama-3.1-8b-instant")  # default fallback

app = FastAPI(
    title="Mini AI Interview Screener",
    description="Evaluates and ranks candidate answers using Groq LLM",
    version="1.0"
)

# ------------ REQUEST MODELS -----------------
class AnswerRequest(BaseModel):
    answer: str

class CandidateList(BaseModel):
    answers: list[str]


# ------------ LLM EVALUATOR CORE LOGIC ----------------
def evaluate_answer_llm(answer: str) -> dict:
    prompt = f"""
You are an interview evaluator. Return STRICT JSON only:

{{
  "score": 1-5,
  "summary": "One-line summary",
  "improvement": "One improvement suggestion"
}}

Candidate answer: "{answer}"
"""
    try:
        res = client.chat.completions.create(
            model=MODEL,
            messages=[{"role":"user","content":prompt}],
            temperature=0.2
        )
        output = res.choices[0].message.content.strip()
        return json.loads(output)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {e}")


# ------------ API ROUTES ----------------
@app.post("/evaluate-answer")
def evaluate(data: AnswerRequest):
    return evaluate_answer_llm(data.answer)

@app.post("/rank-candidates")
def rank(data: CandidateList):
    results = [{"answer": a, **evaluate_answer_llm(a)} for a in data.answers]
    ranked = sorted(results, key=lambda x: x["score"], reverse=True)
    return {"ranked_candidates": ranked}
