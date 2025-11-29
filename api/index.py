# api/index.py → required for Vercel serverless deployment

from fastapi import FastAPI
from mangum import Mangum
from app import app  # ← imports your existing FastAPI application from app.py

# Vercel serverless handler
handler = Mangum(app)


# Optional: Root endpoint to verify deployment works
@app.get("/")
def home():
    return {"message": "Mini AI Interview Screener Backend is Live 🚀"}
