#!/usr/bin/env python3
"""Update generated README sections for a Markdown knowledge base.

This script is deterministic: it scans the repository tree, builds a folder/file
structure, builds a grouped article index, and replaces only the content between
README marker comments.

Markers expected in README.md:

<!-- STRUCTURE_START -->
<!-- STRUCTURE_END -->
<!-- ARTICLES_START -->
<!-- ARTICLES_END -->
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Iterable

IGNORE_DIRS = {
    ".git",
    ".github",
    ".vscode",
    ".idea",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
}

IGNORE_FILES = {
    "README-marker-snippet.md",
}

STRUCTURE_START = "<!-- STRUCTURE_START -->"
STRUCTURE_END = "<!-- STRUCTURE_END -->"
ARTICLES_START = "<!-- ARTICLES_START -->"
ARTICLES_END = "<!-- ARTICLES_END -->"


def should_skip(path: Path, repo_root: Path) -> bool:
    rel_parts = path.relative_to(repo_root).parts
    if any(part in IGNORE_DIRS for part in rel_parts):
        return True
    if path.name in IGNORE_FILES:
        return True
    return False


def markdown_title(path: Path) -> str:
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except UnicodeDecodeError:
        pass
    return path.stem.replace("-", " ").replace("_", " ").title()


def iter_markdown_articles(repo_root: Path) -> list[Path]:
    articles: list[Path] = []
    for path in repo_root.rglob("*.md"):
        if should_skip(path, repo_root):
            continue
        if path.name == "README.md":
            continue
        articles.append(path)
    return sorted(articles, key=lambda p: str(p.relative_to(repo_root)).lower())


def build_tree(repo_root: Path) -> str:
    """Build a simple tree containing directories and Markdown files."""
    lines = [repo_root.name + "/"]

    def walk(directory: Path, prefix: str = "") -> None:
        children = []
        for child in sorted(directory.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower())):
            if should_skip(child, repo_root):
                continue
            if child.is_dir():
                # Include dirs if they contain at least one non-ignored Markdown file or useful child dir.
                if any(not should_skip(p, repo_root) and (p.is_dir() or p.suffix == ".md") for p in child.rglob("*")):
                    children.append(child)
            elif child.suffix == ".md" and child.name != "README-marker-snippet.md":
                children.append(child)

        for index, child in enumerate(children):
            connector = "└── " if index == len(children) - 1 else "├── "
            extension = "    " if index == len(children) - 1 else "│   "
            if child.is_dir():
                lines.append(f"{prefix}{connector}{child.name}/")
                walk(child, prefix + extension)
            else:
                lines.append(f"{prefix}{connector}{child.name}")

    walk(repo_root)
    return "```text\n" + "\n".join(lines) + "\n```"


def category_name(path: Path, repo_root: Path) -> str:
    rel = path.relative_to(repo_root)
    if len(rel.parts) <= 1:
        return "Root"
    return rel.parts[0].replace("-", " ").replace("_", " ").title()


def build_articles(repo_root: Path) -> str:
    articles = iter_markdown_articles(repo_root)
    if not articles:
        return "No articles found yet."

    grouped: dict[str, list[Path]] = {}
    for article in articles:
        grouped.setdefault(category_name(article, repo_root), []).append(article)

    lines: list[str] = []
    for category in sorted(grouped):
        lines.append(f"### {category}")
        for article in grouped[category]:
            rel = article.relative_to(repo_root).as_posix()
            title = markdown_title(article)
            lines.append(f"- [{title}]({rel})")
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_between_markers(content: str, start: str, end: str, replacement: str) -> str:
    if start not in content or end not in content:
        raise ValueError(f"Missing README markers: {start} and/or {end}")

    before, remainder = content.split(start, 1)
    _old, after = remainder.split(end, 1)
    return f"{before}{start}\n{replacement}\n{end}{after}"


def update_readme(repo_root: Path, readme_path: Path) -> bool:
    original = readme_path.read_text(encoding="utf-8")
    updated = replace_between_markers(original, STRUCTURE_START, STRUCTURE_END, build_tree(repo_root))
    updated = replace_between_markers(updated, ARTICLES_START, ARTICLES_END, build_articles(repo_root))

    if updated != original:
        readme_path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Update README generated index sections.")
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    parser.add_argument("--readme", default="README.md", help="README path relative to repo root")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    readme_path = (repo_root / args.readme).resolve()

    changed = update_readme(repo_root, readme_path)
    print("README updated." if changed else "README already up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
