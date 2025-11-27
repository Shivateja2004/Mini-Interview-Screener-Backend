# 🧠 Mini AI Interview Screener (Backend Only)

A lightweight backend API that evaluates candidate answers using an LLM and ranks applicants based on performance.  
Built as part of the **48-Hour Engineering Assignment — VantaHire | AI Revo Labs**.

---

## 🚀 Features

| Feature | Status |
|---|---|
| Evaluate candidate answer using LLM | ✔ |
| Score (1–5) + summary + improvement feedback | ✔ |
| Rank multiple applicants based on score | ✔ |
| Clean JSON responses | ✔ |
| Fully testable via Swagger UI | ✔ |

---

## 🛠 Tech Stack + Why Chosen

| Technology | Purpose | Why chosen |
|---|---|---|
| **Python** | Core backend | Fast development & clean logic |
| **FastAPI** | API framework | Auto docs, async, modern, scalable |
| **Groq LLM API** | AI evaluation | Fast inference, structured output |
| **Uvicorn** | ASGI server | Lightweight and production-ready |

> Decision Thinking:  
FastAPI helped deliver functionality quickly with zero UI requirement.  
Groq LLM ensured instant responses without token billing concerns.
Python gave flexibility to implement ranking logic reliably under time pressure.

---

## 📂 Project Structure

```
mini-ai-interview-screener/
│── app.py                # Main API application
│── requirements.txt      # Dependencies list
│── .env                  # Keys/Config (not pushed to GitHub)
│── README.md             # Documentation
```

---

## 💾 Installation & Setup

### 1️⃣ Clone the project

```bash
git clone <your-repo-url>
cd mini-ai-interview-screener
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create **.env** file (required)

```
GROQ_API_KEY='API'
MODEL=llama-3.1-8b-instant
```

### 5️⃣ Run Server

```bash
uvicorn app:app --reload
```

### Access API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🔥 API Endpoints

### 1️⃣ /evaluate-answer

**POST Body:**

```json
{
  "answer": "I would design microservices with caching & load balancing."
}
```

**Sample Output:**

```json
{
  "score": 4,
  "summary": "Good understanding of scalable systems",
  "improvement": "Explain deeper implementation strategy"
}
```

---

### 2️⃣ /rank-candidates

**POST Body:**

```json
{
  "answers": [
    "I design scalable services.",
    "I use performance optimization.",
    "I build modular backend systems."
  ]
}
```

**Output Example:**

```json
{
  "ranked_candidates": [
    { "answer": "...", "score": 5, "summary": "...", "improvement": "..."},
    { "answer": "...", "score": 4, "summary": "...", "improvement": "..."},
    { "answer": "...", "score": 3, "summary": "...", "improvement": "..."}
  ]
}
```

---

## 📜 Evaluation Criteria Covered

| Requirement | Completed |
|---|---|
| Integrate LLM | ✔ |
| Score + Evaluate Answers | ✔ |
| Ranking Function | ✔ |
| JSON Responses | ✔ |
| Clean API Structure | ✔ |
| Documentation + Setup | ✔ |

---

