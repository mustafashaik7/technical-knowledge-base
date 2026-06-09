# Deterministic Automation vs Agentic AI Workflows

## Objective

This article explains when to use deterministic automation and when to use an Agentic AI workflow. It also shows how this applies to a practical knowledge base repository where the root `README.md` must stay updated as articles and folders change.

## Short Answer

Use deterministic automation when the task is rule-based, repeatable, and verifiable. Use Agentic AI when the task requires judgment, interpretation, planning, summarization, or adaptation.

For keeping a README's `Current Structure` and `Articles` sections updated, deterministic automation is the right first choice.

## Decision Rule

| Need | Better approach | Why |
|---|---|---|
| List folders and files | Deterministic automation | Rules are clear and repeatable |
| Generate Markdown links | Deterministic automation | Output can be derived exactly |
| Sort articles by category | Deterministic automation | No reasoning needed |
| Summarize an article | Agentic AI | Requires language understanding |
| Suggest tags | Agentic AI | Requires interpretation |
| Detect stale content | Hybrid | Rules detect age; AI can assess meaning |
| Rewrite rough notes into a polished guide | Agentic AI with human review | Requires judgment and writing quality |

## Practical Repo Scenario

Assume the existing repository is:

```text
technical-knowledge-base/
```

The automation PoC lives inside the parent repository as:

```text
technical-knowledge-base/automation/deterministic-automation-vs-agentic-ai-workflow/
```

The GitHub Actions workflow lives at:

```text
technical-knowledge-base/.github/workflows/update-readme-index.yml
```

This workflow updates the root:

```text
technical-knowledge-base/README.md
```

whenever the repository structure or Markdown articles change.

## Recommended Architecture

```text
Developer adds or updates Markdown article
        |
        v
Git push to main
        |
        v
GitHub Actions workflow runs
        |
        v
Python script scans repository structure
        |
        v
README Current Structure and Articles sections are regenerated
        |
        v
Workflow commits README.md update
```

## Why This Is Not Agentic AI

The task has clear rules:

1. Find Markdown files.
2. Ignore selected folders.
3. Build a tree.
4. Build article links.
5. Replace text between known markers.

No reasoning is required. No LLM is required. No token cost is required.

## Where Agentic AI Fits Later

Agentic AI becomes useful when the workflow needs to understand the article content.

Examples:

| Agentic enhancement | What the AI does |
|---|---|
| Generate article summary | Reads the article and writes a short abstract |
| Suggest tags | Identifies topics such as GCP, Terraform, GitHub, RAG |
| Recommend related articles | Compares content across notes |
| Check article quality | Flags missing validation, cleanup, or troubleshooting sections |
| Identify stale content | Looks for version-sensitive or date-sensitive claims |

## Tools and Techniques

### Deterministic automation tools

- Python
- Bash
- GitHub Actions
- Markdown markers
- markdownlint
- link checkers
- pre-commit hooks

### Agentic AI tools

- LLM API or local model
- structured JSON output
- schema validation
- RAG over the repository
- pull-request based human review
- cost and token monitoring

## Cost Considerations

### Deterministic automation

For a small public GitHub repository, deterministic README updates are typically very low cost. The script runs quickly and does not call any external AI service.

Main costs:

- GitHub Actions minutes, if applicable
- negligible compute time
- engineering setup time

### Agentic AI workflow

Agentic AI adds variable cost.

Main costs:

- LLM input and output tokens
- embedding costs if RAG is used
- vector database or storage costs if used
- additional GitHub Actions runtime
- review and governance effort

## Recommended Implementation Strategy

Start with deterministic automation:

```text
README index update = Python script + GitHub Actions
```

Then add Agentic AI only after there is a clear need:

```text
Article metadata enrichment = LLM + schema validation + pull request review
```

## Exam and Portfolio Relevance

This project is useful for cloud, DevOps, and Agentic AI portfolios because it demonstrates the ability to choose the right automation level.

A strong engineering statement would be:

> I used deterministic automation for predictable repository indexing and reserved Agentic AI for future content-understanding tasks such as summarization, tagging, and stale-content detection.

## Key Takeaway

Do not use AI where rules are enough. Use Agentic AI where judgment is required.
