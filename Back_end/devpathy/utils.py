# File: devpathy/utils.py
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from textwrap import dedent
from typing import List, Dict, Any


@dataclass
class InputPayload:
    code_snippet: str
    review_comments: List[str]


def load_input(path: str | None) -> InputPayload:
    """Load JSON from file or stdin.
    Why: predictable IO for hackathon judges; avoids surprises.
    """
    data: Dict[str, Any]
    if path and path != "-":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object with keys 'code_snippet' and 'review_comments'.")

    code = dedent(str(data.get("code_snippet", "")))
    comments = data.get("review_comments", [])
    if not isinstance(comments, list) or not all(isinstance(c, str) for c in comments):
        raise ValueError("'review_comments' must be a list of strings.")

    return InputPayload(code_snippet=code, review_comments=comments)


def write_output(markdown: str, path: str | None) -> None:
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(markdown)
    else:
        sys.stdout.write(markdown)


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="devpathy",
        description="Devpathy — Empathetic Code Reviewer: JSON -> Markdown report",
    )
    p.add_argument("--input", "-i", help="Path to input JSON (or '-' for stdin)", default="-")
    p.add_argument("--output", "-o", help="Path to output Markdown (omit for stdout)")
    p.add_argument("--links", action="store_true", help="Append resource links section")
    p.add_argument("--style", choices=["friendly", "neutral", "direct"], default="friendly",
                   help="Base tone style; severity still adjusts phrasing")
    return p