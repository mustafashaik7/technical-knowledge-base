# Local LLM Prompt-Injection Evaluation

This project evaluates whether a locally deployed language model can act as a semantic input guard for another model. It compares a short, underspecified guard policy with a hardened policy that decomposes attack categories, defines authority rules, handles mixed-intent requests, and returns constrained JSON.

The evaluation uses LangChain-era practicum concepts with local inference through Ollama. The reproducible supplementary run uses `llama3.2:3b`, 12 adversarial prompts, and 12 benign controls.

## Results at a Glance

| Metric | Naive guard | Hardened guard |
| --- | ---: | ---: |
| Attacks blocked | 2 of 12 | 9 of 12 |
| Detection rate | 16.7% | 75.0% |
| Benign prompts blocked | 1 of 12 | 0 of 12 |
| Balanced accuracy | 54.2% | 87.5% |
| Mean guard latency | 0.343 s | 0.416 s |

These figures describe a small 24-case corpus. They are exploratory results, not population-level safety estimates or a security certification.

## What Is Included

- [`REPORT.md`](REPORT.md) contains the concise project report.
- [`report/project-report.pdf`](report/project-report.pdf) is the fixed-layout, two-page version.
- [`scripts/run_supplementary_eval.py`](scripts/run_supplementary_eval.py) runs the naive guard, target model, and response judge.
- [`scripts/run_hardened_guard_eval.py`](scripts/run_hardened_guard_eval.py) evaluates the hardened guard on the same corpus.
- [`results/supplementary_eval_results.json`](results/supplementary_eval_results.json) contains prompts, model outputs, classifications, latency measurements, and summary statistics.

## Reproduce the Evaluation

Install [Ollama](https://ollama.com/), then pull and start the model.

```bash
ollama pull llama3.2:3b
ollama serve
```

From this project directory, run:

```bash
python3 scripts/run_supplementary_eval.py
python3 scripts/run_hardened_guard_eval.py
```

Both scripts use only the Python standard library. Ollama must be available at `http://127.0.0.1:11434`.

## Provenance and Scope

The original Georgia Tech M.S. Cybersecurity practicum examined prompt-injection defenses for locally deployed LLM applications using LangChain and Ollama. Its executable repository and numerical result tables were not preserved in the materials available for this publication.

The quantitative results in this repository come from a supplementary evaluation run in October 2026 using a recovered adversarial prompt artifact and an available local model. They should not be attributed to the archived course results.

The supplementary corpus measures direct user-prompt attacks. Indirect injection through retrieved content, multi-turn attacks, tool-mediated effects, and memory poisoning remain future work.

## Responsible Use

The adversarial prompts are included for defensive evaluation. Do not connect the target model to production tools, sensitive data, credentials, or external actions when reproducing this experiment.

