# File: devpathy/cli.py
from __future__ import annotations

from .utils import build_arg_parser, load_input, write_output
from .core import generate_report


def main() -> None:
    args = build_arg_parser().parse_args()
    payload = load_input(args.input)
    md = generate_report(
        code_snippet=payload.code_snippet,
        review_comments=payload.review_comments,
        base_style=args.style,
        include_links=args.links,
    )
    write_output(md, args.output)


if __name__ == "__main__":
    main()
