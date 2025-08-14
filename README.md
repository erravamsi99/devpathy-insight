Here’s a **single README.md** for your full project (backend + frontend) in the new root-level structure.
It’s hackathon-friendly, clearly explains what Devpathy does, and gives judges quick run + deploy instructions.

---

```markdown
# 💙 Devpathy — The Empathetic Code Reviewer

**Theme:** Freedom from Mundane: AI for a Smarter Life  
**Mission:** Transform blunt, critical code review comments into empathetic, constructive, and educational feedback using **Generative AI**.

---

## 📖 Overview
Devpathy takes a **code snippet** and a list of **direct review comments**, and rewrites them in a way that:
1. Encourages and motivates the developer.
2. Explains the reasoning (“The Why”) clearly and technically.
3. Suggests concrete improvements with example code.

It has **two modes**:
- **GPT Mode** — Uses OpenAI GPT for natural, nuanced rewrites (requires `OPENAI_API_KEY`).
- **Offline Mode** — Uses an intelligent, rule-based system with category-specific suggestions.

---

## 🗂 Project Structure
```

Devpathy/
├── backend/               # Python FastAPI backend
│   ├── main.py             # FastAPI entry point
│   ├── devpathy/           # Core Python package
│   │   ├── core.py
│   │   ├── rules.py
│   │   └── ...
│   └── requirements.txt    # Backend dependencies
│
├── frontend/              # React + Tailwind frontend
│   ├── package.json
│   ├── src/
│   └── ...
│
└── README.md              # This file

````

---

## 🚀 Features
- 🔹 **Dynamic tone adjustment** based on comment severity & style.
- 🔹 **Category-aware explanations** (performance, naming, pythonic, duplication, complexity, style).
- 🔹 **Markdown-formatted reports** with code blocks.
- 🔹 **Frontend UI** for pasting JSON and previewing reports.
- 🔹 **Single-deploy ready** — serve frontend & backend together.

---

## 📦 Backend Setup

### 1. Install dependencies
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Mac/Linux
pip install --upgrade pip
pip install -r requirements.txt
````

### 2. (Optional) Set OpenAI API key

```bash
# Windows PowerShell
setx OPENAI_API_KEY "your-key-here"

# Mac/Linux
export OPENAI_API_KEY="your-key-here"
```

### 3. Run backend

```bash
cd ..
uvicorn backend.main:app --reload --port 8000
```

Visit: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** for API docs.

---

## 🎨 Frontend Setup

### 1. Install dependencies

```bash
cd frontend
npm install
```

### 2. Update API URL

In `src/api.js`, set the backend URL:

```js
const API_URL = "http://127.0.0.1:8000/generate";
```

### 3. Run frontend

```bash
npm run dev
```

Visit: **[http://localhost:5173](http://localhost:5173)**

---

## 🖇 Connecting Frontend & Backend Locally

1. Start backend → `uvicorn backend.main:app --reload --port 8000`
2. Start frontend → `npm run dev`
3. Paste JSON payload in UI, click **Generate Report** → see Markdown output.

---

## 🌐 Single Deploy (Frontend + Backend Together)

1. Build frontend:

```bash
cd frontend
npm run build
```

2. Copy `frontend/dist` into `backend/static` (or configure FastAPI to serve it).
3. Deploy backend to Render/Railway — it will serve both UI and API at one URL.

---

## 📝 Example Input

```json
{
  "code_snippet": "def get_active_users(users):\n    results = []\n    for u in users:\n        if u.is_active == True and u.profile_complete == True:\n            results.append(u)\n    return results",
  "review_comments": [
    "This is inefficient. Don't loop twice conceptually.",
    "Variable 'u' is a bad name.",
    "Boolean comparison '== True' is redundant."
  ]
}
```

---

## 🏆 Hackathon Scoring Alignment

* **Functionality & Correctness (25%)** — Works both offline & with GPT.
* **Quality of AI Output (45%)** — Empathetic, educational rewrites.
* **Code Quality (20%)** — Clean, modular Python & React code.
* **Innovation (10%)** — Severity-based tone, category-aware explanations, and single-deploy capability.

---

## 📚 Resources

* [PEP 8 — Python Style Guide](https://peps.python.org/pep-0008/)
* [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Vite + React Docs](https://vitejs.dev/guide/)

```

---

I can now also give you a **FastAPI config** so that when you run `uvicorn backend.main:app` it will serve **both your React build and the `/generate` API** — meaning you’ll have just **one deploy URL** for the judges.  

Do you want me to set up that unified deployment version? That will make your hackathon demo super smooth.
```

