# File: README.md

# Devpathy — The Empathetic Code Reviewer

Devpathy transforms blunt code review comments into empathetic, constructive, and educational guidance.
It ingests a JSON object with a code snippet and review comments, then outputs a well-structured Markdown report
covering: Positive Rephrasing, The Why, and Suggested Improvement (with code examples).

> Mission: Hackathon Mission 1 — "The Empathetic Code Reviewer"

---

## Features
- 🔹 Severity-aware tone (supportive ↔ direct) based on the language of the comment.
- 🔹 Category detection (performance, naming, Pythonic truthiness, duplication, complexity, style).
- 🔹 Concrete code suggestions via pattern-driven snippets.
- 🔹 Holistic summary + resource links (PEP 8, Python idioms, complexity basics).
- 🔹 Clean CLI: file or stdin, stdout or file.

## Quickstart

```bash
python -m devpathy --input examples/sample_input.json --output report.md
cat report.md
```

### Input JSON shape
```json
{
  "code_snippet": "def get_active_users(users):\n    results = []\n    for u in users:\n        if u.is_active == True and u.profile_complete == True:\n            results.append(u)\n    return results\n",
  "review_comments": [
    "This is inefficient. Don't loop twice conceptually.",
    "Variable 'u' is a bad name.",
    "Boolean comparison '== True' is redundant."
  ]
}
```

### Output
- A single Markdown report to stdout or a specified file.

---

## Design Notes
- No external API is required. Devpathy uses rule-based analysis to ensure reliable, offline behavior.
- You can extend `rules.py` to add more detections and improvement snippets.

---

## Project Structure
```
devpathy/
  __init__.py
  cli.py
  core.py
  rules.py
  utils.py
examples/
  sample_input.json
```

---

## Evaluation Alignment
- **Functionality & Correctness**: Deterministic CLI, exact Markdown format.
- **Quality of AI Output**: Severity-aware tone, category-specific "why", actionable code examples.
- **Code Quality & Docs**: Typed, modular, PEP8 friendly, README with clear usage.
- **Innovation**: Rule engine + auto-snippet generation; links to resources; holistic summary.

---

## License
MIT
```

