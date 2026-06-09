#!/usr/bin/env python3
"""Safe placeholder for future agentic metadata enrichment.

This file intentionally does not call an LLM. It documents the extension point
where an agentic workflow could later generate summaries, tags, difficulty, and
related-article suggestions, preferably through a pull request and human review.
"""

from pathlib import Path


def main() -> int:
    print("Agentic metadata enrichment is not enabled.")
    print("Recommended future pattern:")
    print("1. Detect changed Markdown articles.")
    print("2. Send article text to an approved LLM with a strict JSON schema.")
    print("3. Validate generated metadata.")
    print("4. Open a pull request for human review.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
