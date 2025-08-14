# File: devpathy/rules.py
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass(frozen=True)
class Detection:
    category: str  # e.g., performance, naming, pythonic, duplication, complexity, style
    rationale: str
    resource_links: List[str]
    # optional pre-canned suggestion producer key
    suggestion_key: Optional[str] = None


# Precompiled regexes for speed and clarity
_PATTERNS: list[tuple[re.Pattern[str], Detection]] = [
    # Performance / loops
    (
        re.compile(r"\b(inefficient|performance|slow|optimi[sz]e|nested loop)\b", re.I),
        Detection(
            category="performance",
            rationale=(
                "Loop-heavy operations grow with input size; prefer vectorized or comprehension-based constructs "
                "to reduce overhead and improve readability."
            ),
            resource_links=[
                "https://wiki.python.org/moin/TimeComplexity",
                "https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions",
            ],
            suggestion_key="list_comprehension",
        ),
    ),
    # Naming
    (
        re.compile(r"\b(name|naming|bad name|unclear|ambiguous|single[- ]letter var)\b", re.I),
        Detection(
            category="naming",
            rationale=(
                "Descriptive, consistent names improve readability and maintainability; follow PEP 8 naming conventions."
            ),
            resource_links=[
                "https://peps.python.org/pep-0008/#naming-conventions",
            ],
            suggestion_key="rename_var",
        ),
    ),
    # Truthiness / booleans
    (
        re.compile(r"\b==\s*True\b|\b==\s*False\b|\bredundant boolean|truthiness|boolean comparison\b", re.I),
        Detection(
            category="pythonic",
            rationale=(
                "In Python, conditions evaluate truthiness directly; avoid explicit comparisons to True/False for clarity."
            ),
            resource_links=[
                "https://peps.python.org/pep-0008/#programming-recommendations",
            ],
            suggestion_key="truthiness",
        ),
    ),
    # Duplication / DRY
    (
        re.compile(r"\bduplicate|duplication|DRY|copy[- ]paste\b", re.I),
        Detection(
            category="duplication",
            rationale=(
                "Duplicated logic increases bug risk; extract common code into reusable functions to honor DRY."
            ),
            resource_links=[
                "https://refactoring.guru/smells/duplicate-code",
            ],
            suggestion_key="extract_function",
        ),
    ),
    # Complexity
    (
        re.compile(r"\bcomplex|hard to read|readability|cyclomatic|spaghetti\b", re.I),
        Detection(
            category="complexity",
            rationale=(
                "High branching or deeply nested code is error-prone; simplify control flow and prefer small functions."
            ),
            resource_links=[
                "https://refactoring.guru/simplify-conditional",
            ],
            suggestion_key="simplify_conditionals",
        ),
    ),
    # Style
    (
        re.compile(r"\bstyle|pep8|format|whitespace|lint\b", re.I),
        Detection(
            category="style",
            rationale=(
                "Consistent formatting aids scanning and reduces cognitive load; adopt automated formatting and linting."
            ),
            resource_links=[
                "https://peps.python.org/pep-0008/",
                "https://black.readthedocs.io/en/stable/",
            ],
            suggestion_key="formatting",
        ),
    ),
]


def detect(comment: str) -> Detection:
    for pattern, det in _PATTERNS:
        if pattern.search(comment):
            return det
    # Fallback generic detection
    return Detection(
        category="general",
        rationale="Focus on clarity, correctness, and simplicity; justify changes with readability and maintainability in mind.",
        resource_links=["https://peps.python.org/pep-0008/"],
        suggestion_key=None,
    )


# Severity heuristics: map words → 0..2 (low..high)
_SEVERITY_WORDS = {
    2: ["terrible", "awful", "broken", "unacceptable", "never", "worst", "completely wrong"],
    1: ["bad", "inefficient", "wrong", "poor", "confusing", "hacky"],
    0: ["nit", "minor", "optional", "could"],
}


def severity_score(comment: str) -> int:
    c = comment.lower()
    score = 1  # default medium
    for s, words in _SEVERITY_WORDS.items():
        if any(w in c for w in words):
            score = max(score, s)
    # soften if contains courtesy markers
    if any(x in c for x in ["please", "nit", "nit:", "suggestion"]):
        score = min(score, 1)
    return score


# Suggestion snippet producers

def suggest_truthiness(code: str) -> str:
    return (
        "# Prefer direct truthiness checks\n"
        "if obj_is_active:\n    ...\n# instead of\nif obj_is_active == True:\n    ...\n\n"
        "# Negation\nif not is_ready:\n    ...  # rather than: if is_ready == False:\n"
    )


def suggest_list_comprehension(code: str) -> str:
    return (
        "# Example: filter + collect in one pass\n"
        "def get_active_users(users):\n"
        "    return [u for u in users if u.is_active and u.profile_complete]\n"
    )


def suggest_rename_var(code: str) -> str:
    return (
        "# Example: meaningful loop variable\n"
        "for user in users:  # not just 'u'\n"
        "    ...\n"
    )


def suggest_extract_function(code: str) -> str:
    return (
        "# Example: extract reusable predicate\n"
        "def is_active_and_complete(user):\n"
        "    return user.is_active and user.profile_complete\n\n"
        "def get_active_users(users):\n"
        "    return [u for u in users if is_active_and_complete(u)]\n"
    )


def suggest_simplify_conditionals(code: str) -> str:
    return (
        "# Example: early return to reduce nesting\n"
        "def process(x):\n"
        "    if not x:\n        return None\n"
        "    # continue with simple, flat logic...\n"
    )


def suggest_formatting(code: str) -> str:
    return (
        "# Use Black + Ruff (flake8) in CI to enforce style automatically\n"
        "# pip install black ruff\n"
        "# black . && ruff check .\n"
    )


_SUGGESTION_MAP = {
    "truthiness": suggest_truthiness,
    "list_comprehension": suggest_list_comprehension,
    "rename_var": suggest_rename_var,
    "extract_function": suggest_extract_function,
    "simplify_conditionals": suggest_simplify_conditionals,
    "formatting": suggest_formatting,
}


def render_suggestion(key: Optional[str], code: str) -> str:
    if key and key in _SUGGESTION_MAP:
        return _SUGGESTION_MAP[key](code)
    # generic fallback
    return (
        "# Example: targeted revision\n"
        "# 1) Describe the change in one sentence\n"
        "# 2) Show a small, focused snippet illustrating it\n"
    )
