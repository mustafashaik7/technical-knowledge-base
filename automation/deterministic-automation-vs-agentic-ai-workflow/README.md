# README Index Automation PoC

This folder contains a drop-in automation pattern for the parent repository `technical-knowledge-base`.

The goal is to keep the root `README.md` up to date whenever the knowledge base structure changes.

## Why this lives inside the parent repo

The parent repo is the source of truth. The automation code can live under:

```text
technical-knowledge-base/automation/deterministic-automation-vs-agentic-ai-workflow/
```

But the GitHub Actions workflow must live at the parent repo root:

```text
technical-knowledge-base/.github/workflows/update-readme-index.yml
```

GitHub only discovers workflows from `.github/workflows` at the repository root.

## What the deterministic workflow does

1. Runs when Markdown or automation files change on `main`.
2. Scans the repository tree.
3. Generates the `Current Structure` section.
4. Generates the `Articles` section.
5. Updates only the content between README marker comments.
6. Commits the README update back to the repository.

## What it does not do

It does not use AI to summarize, classify, or rewrite articles. That is intentional. Structure and article indexing are deterministic tasks, so a Python script is safer, cheaper, and more reliable.

## Where Agentic AI could be added later

The included `agentic_metadata_stub.py` shows a future extension point for:

- article summaries
- topic tags
- difficulty levels
- related articles
- stale-content warnings

Those changes should be opened as pull requests for human review, not committed blindly.

## Local test

From the root of `technical-knowledge-base`:

```bash
python automation/deterministic-automation-vs-agentic-ai-workflow/scripts/update_readme_index.py --repo-root . --readme README.md
```

Then review:

```bash
git diff README.md
```
