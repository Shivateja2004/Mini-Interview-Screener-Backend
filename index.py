from fastapi import FastAPI
from app import evaluate_answer_llm, AnswerRequest, CandidateList

app = FastAPI()

@app.post("/evaluate-answer")
def evaluate(data: AnswerRequest):
    return evaluate_answer_llm(data.answer)

@app.post("/rank-candidates")
def rank(data: CandidateList):
    results = [{"answer": ans, **evaluate_answer_llm(ans)} for ans in data.answers]
    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return {"ranked": results}

# Export handler for vercel
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

handler = Mangum(app)
