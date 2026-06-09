# Technical Knowledge Base

A personal technical knowledge base for documenting hands-on learning, troubleshooting notes, cloud labs, AI certification preparation, and reusable engineering procedures.

This repository is intended to be owned under the GitHub account `mustafashaik7` and maintained as a Markdown-based source of truth.

## Repository Purpose

This knowledge base helps organize practical technical notes into reusable articles that can be referenced later, shared publicly, and linked from portfolio projects.

It is designed for topics such as:

- Git and GitHub workflows
- Cloud networking and infrastructure labs
- Terraform and Infrastructure as Code
- AI certification preparation
- Troubleshooting guides
- Repeatable command-line procedures

## Current Structure

<!-- STRUCTURE_START -->
```text
technical-knowledge-base/
├── ai-agents/
│   └── deterministic-automation-vs-agentic-ai-workflows.md
├── ai-certifications/
│   └── nvidia-ncp-aai-study-plan.md
├── automation/
│   └── deterministic-automation-vs-agentic-ai-workflow/
│       └── README.md
├── git-github/
│   └── multiple-github-accounts-ssh.md
├── templates/
│   ├── knowledge-article-template.md
│   └── troubleshooting-template.md
└── README.md
```
<!-- STRUCTURE_END -->

## Articles

<!-- ARTICLES_START -->
### Ai Agents
- [Deterministic Automation vs Agentic AI Workflows](ai-agents/deterministic-automation-vs-agentic-ai-workflows.md)

### Ai Certifications
- [NVIDIA Certified Professional - Agentic AI (NCP-AAI) Study Plan](ai-certifications/nvidia-ncp-aai-study-plan.md)

### Git Github
- [Maintain Two GitHub Accounts Simultaneously Using SSH](git-github/multiple-github-accounts-ssh.md)

### Templates
- [<Knowledge Article Title>](templates/knowledge-article-template.md)
- [Troubleshooting: <Issue Title>](templates/troubleshooting-template.md)
<!-- ARTICLES_END -->

### Git and GitHub

- [Managing Multiple GitHub Accounts with SSH](git-github/multiple-github-accounts-ssh.md)

### AI Certifications

- [NVIDIA NCP-AAI Certification Study Plan](ai-certifications/nvidia-ncp-aai-study-plan.md)

### Templates

- [Knowledge Article Template](templates/knowledge-article-template.md)
- [Troubleshooting Template](templates/troubleshooting-template.md)

## Recommended Writing Standard

Each article should be written in a practical, reusable format:

1. Objective or problem statement
2. Environment and assumptions
3. Key concepts
4. Step-by-step implementation
5. Validation commands or checks
6. Troubleshooting notes
7. Cleanup steps, if applicable
8. References or related links

## Security Guidelines

Never commit sensitive information to this repository.

Do not store:

- Passwords
- API keys
- GitHub tokens
- Private SSH keys
- Cloud service account keys
- Customer or employer confidential information
- Screenshots containing secrets, internal hostnames, private data, or credentials

Use placeholders instead, for example:

```text
<YOUR_PUBLIC_IP>
<PROJECT_ID>
<REPOSITORY_NAME>
<PRIVATE_KEY_PATH>
```

## Suggested Git Workflow

```bash
git init
git add .
git commit -m "Initial technical knowledge base"
git branch -M main
git remote add origin git@github-mustafa:mustafashaik7/technical-knowledge-base.git
git push -u origin main
```

Use the `github-mustafa` SSH alias if you maintain multiple GitHub accounts on the same machine.

## Portfolio Note

This repository can be used as a professional portfolio artifact because it demonstrates:

- Documentation discipline
- Troubleshooting ability
- Cloud and AI learning progress
- GitHub and Markdown fluency
- Reusable technical communication skills
