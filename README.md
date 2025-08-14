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
├── Back\_end/              # Python FastAPI backend
│   ├── main.py             # FastAPI entry point
│   ├── devpathy/           # Core Python package
│   │   ├── core.py
│   │   ├── rules.py
│   │   └── ...
│   └── requirements.txt    # Backend dependencies
│
├── public/                 # Frontend public assets
├── src/                    # Frontend source code
├── index.html              # Frontend HTML entry point
├── package.json            # Frontend dependencies
├── vite.config.ts          # Vite config
├── tailwind.config.ts      # Tailwind config
└── README.md               # This file

````

---

## 🚀 Features
- 🔹 **Dynamic tone adjustment** based on comment severity & style.
- 🔹 **Category-aware explanations** (performance, naming, pythonic, duplication, complexity, style).
- 🔹 **Markdown-formatted reports** with code blocks.
- 🔹 **Frontend UI** for pasting JSON and previewing reports.
- 🔹 **Hackathon-ready** — Works locally and with a live backend.

---

## 📦 Backend Setup

### 1. Install dependencies
```bash
cd Back_end
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
uvicorn Back_end.main:app --reload --port 8000
```

Visit: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)** for API docs.

---

## 🎨 Frontend Setup

### 1. Install dependencies

```bash
npm install
```

### 2. Update API URL

In `src/api.ts`, set the backend URL:

```ts
const API_URL = "http://127.0.0.1:8000/generate";
```

### 3. Run frontend

```bash
npm run dev
```

Visit: **[http://localhost:5173](http://localhost:5173)**

---

## 🖇 Connecting Frontend & Backend Locally

1. Start backend → `uvicorn Back_end.main:app --reload --port 8000`
2. Start frontend → `npm run dev`
3. Paste JSON payload in UI, click **Generate Report** → see Markdown output.

---

## 📝 Example Input

```json
{
  "code_snippet": "def add(a,b): return a+b",
  "review_comments": [
    "Use better variable names",
    "Missing type hints"
  ],
  "style": "friendly",
  "links": true
}
```

---

## 🏆 Hackathon Scoring Alignment

* **Functionality & Correctness (25%)** — Works both offline & with GPT.
* **Quality of AI Output (45%)** — Empathetic, educational rewrites.
* **Code Quality (20%)** — Clean, modular Python & React code.
* **Innovation (10%)** — Severity-based tone, category-aware explanations.

---

## 📚 Resources

* [PEP 8 — Python Style Guide](https://peps.python.org/pep-0008/)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Vite + React Docs](https://vitejs.dev/guide/)

```

---

If you want, I can **add a section for deployment** that matches your exact structure so you can either:  
- Deploy backend and frontend separately, or  
- Serve frontend build from your `Back_end` FastAPI app for a single hackathon URL.  

Do you want me to add that deployment section now? That way your README covers both cases for the judges.
```
