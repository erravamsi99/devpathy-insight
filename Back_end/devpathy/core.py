# devpathy/core.py
import os
from dataclasses import dataclass
from typing import List
from openai import OpenAI
from .rules import detect, severity_score, render_suggestion

# Initialize client if API key exists
client = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("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"))

@dataclass
class Section:
    comment: str
    positive: str
    why: str
    suggestion_code: str

# Tone templates by severity and base style
TONE_MATRIX = {
    "friendly": {
        0: "Use a light, encouraging tone, focusing on polishing details and reinforcing good habits.",
        1: "Use a warm, constructive tone, showing appreciation for the approach but explaining improvements clearly.",
        2: "Be direct but still supportive, acknowledging effort while emphasizing the importance of fixing this issue quickly."
    },
    "neutral": {
        0: "Use a neutral, professional tone, pointing out small refinements without overemphasis.",
        1: "Be factual and clear, explaining improvements in a concise and respectful manner.",
        2: "Be firm and clear, highlighting that this is important to address for quality."
    },
    "direct": {
        0: "Be brief and matter-of-fact, noting the small improvement plainly.",
        1: "Be clear and concise, explaining the fix without sugarcoating.",
        2: "Be assertive and straightforward, stating the need for an immediate fix."
    }
}

# Category focus mapping
CATEGORY_FOCUS = {
    "performance": "Explain performance considerations, time complexity, and potential optimizations.",
    "naming": "Highlight the importance of descriptive, PEP8-compliant naming conventions.",
    "pythonic": "Explain Pythonic idioms and why they improve clarity and maintainability.",
    "duplication": "Discuss DRY principles and the benefits of code reuse.",
    "complexity": "Explain simplifying complex logic for maintainability and reduced error risk.",
    "style": "Discuss formatting, linting, and style consistency for team collaboration.",
    "general": "Focus on overall clarity, maintainability, and correctness."
}

def ai_rewrite_feedback(comment: str, code: str, style: str, severity: int, category: str) -> str:
    """Use GPT to rewrite feedback with empathy, clarity, and category-specific focus."""
    tone_instruction = TONE_MATRIX.get(style, TONE_MATRIX["friendly"]).get(severity)
    focus_instruction = CATEGORY_FOCUS.get(category, CATEGORY_FOCUS["general"])
    
    prompt = f"""
You are an empathetic senior developer performing a code review.

Given the following code and blunt review comment, rewrite the feedback as a Markdown section with this structure:

### Analysis of Comment: "{comment}"

* **Positive Rephrasing:** Provide encouragement using the tone described below.
* **The 'Why':** Give a clear, technical explanation with depth, focusing on the category provided.
* **Suggested Improvement:** Show a concrete, improved code snippet. Make it specific and directly applicable.

Tone to use: {tone_instruction}
Category to focus on: {focus_instruction}

CODE:
{code}
"""
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return resp.choices[0].message["content"]

def generate_report(code_snippet: str, review_comments: List[str],
                    base_style: str = "friendly", include_links: bool = True) -> str:
    use_gpt = client is not None
    lines: List[str] = []
    lines.append("# Devpathy — Empathetic Code Review Report\n")
    lines.append("_Transforming critical feedback into constructive growth._\n")

    lines.append("\n## Input Code Snippet\n")
    lines.append("```python\n" + code_snippet.rstrip() + "\n```\n")

    if use_gpt:
        for c in review_comments:
            det = detect(c)
            sev = severity_score(c)
            gpt_section = ai_rewrite_feedback(c, code_snippet, base_style, sev, det.category)
            lines.append("\n---\n")
            lines.append(gpt_section)
    else:
        # Offline fallback (existing rule-based logic)
        from .core_offline import offline_analysis
        lines.append(offline_analysis(code_snippet, review_comments, base_style, include_links))

    return "\n".join(lines)
