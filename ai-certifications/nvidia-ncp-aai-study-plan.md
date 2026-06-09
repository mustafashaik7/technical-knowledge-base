# NVIDIA Certified Professional - Agentic AI (NCP-AAI) Study Plan

## 1. Purpose

This article provides a reusable preparation plan for the **NVIDIA Certified Professional - Agentic AI (NCP-AAI)** certification. It is designed as:

- **14 days of structured study**
- **1 week of practice exams and review**
- A focus on **official NVIDIA learning resources**, free resources where available, NVIDIA-specific product knowledge, and exam-style preparation

Use this as a knowledge-base article and adjust the schedule based on your available study hours.

---

## 2. Official Exam Overview

Official certification page:

- NVIDIA Certified Professional - Agentic AI: https://www.nvidia.com/en-eu/learn/certification/agentic-ai-professional/

Key exam facts from NVIDIA:

| Item | Details |
|---|---|
| Certification | NVIDIA Certified Professional - Agentic AI |
| Level | Professional |
| Format | Online, remotely proctored |
| Duration | 120 minutes |
| Questions | 60-70 |
| Language | English |
| Validity | 2 years |
| Recommended experience | 1-2 years in AI/ML roles and hands-on production-level agentic AI work |

Official exam topics include agent design, cognition, planning, memory, knowledge integration, agent development, NVIDIA platform implementation, deployment, evaluation, monitoring, maintenance, safety, compliance, and human oversight.

---

## 3. Exam Blueprint

Use the blueprint to decide how much time to spend on each topic.

| Domain | Weight | What to Know |
|---|---:|---|
| Agent Architecture and Design | 15% | Agent patterns, multi-agent workflows, communication, orchestration |
| Agent Development | 15% | Tool use, prompts, function calling, reliable agent implementation |
| Evaluation and Tuning | 13% | Metrics, benchmarking, RAG evaluation, agent evaluation, tuning loops |
| Deployment and Scaling | 13% | Production deployment, inference serving, scaling, latency, cost, reliability |
| Cognition, Planning, and Memory | 10% | Reasoning, planning, short-term memory, long-term memory, task decomposition |
| Knowledge Integration and Data Handling | 10% | RAG, embeddings, vector databases, reranking, structured/unstructured data |
| NVIDIA Platform Implementation | 7% | NIM, NeMo, NeMo Retriever, NeMo Guardrails, NGC, API Catalog |
| Run, Monitor, and Maintain | 5% | Logs, traces, metrics, troubleshooting, rollback, lifecycle operations |
| Safety, Ethics, and Compliance | 5% | Guardrails, policy controls, privacy, responsible AI, compliance patterns |
| Human-AI Interaction and Oversight | 5% | Human-in-the-loop, approval gates, escalation, UX for agent supervision |

High-yield takeaway:

> The first six domains represent most of the exam. Prioritize agent architecture, development, evaluation, deployment, planning/memory, and RAG/data handling before memorizing product details.

---

## 4. Official NVIDIA-Recommended Training Path

NVIDIA lists the following recommended training for the NCP-AAI certification:

| Resource | Type | Link | Why It Matters |
|---|---|---|---|
| Building RAG Agents With LLMs | Self-paced / instructor-led | https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-15+V1 | Core RAG and agentic RAG foundation |
| Evaluating RAG and Semantic Search Systems | Self-paced | https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-16+V1 | Evaluation and tuning for retrieval and semantic search |
| Building Agentic AI Applications With LLMs | Self-paced / instructor-led | https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-18+V1 | Agent design, orchestration, tools, and production patterns |
| Adding New Knowledge to LLMs | Instructor-led | https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-14+V1 | Knowledge adaptation, RAG vs tuning, domain-specific data |
| Introduction to Deploying RAG Pipelines for Production at Scale | Self-paced / instructor-led | https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-17+V1 | Deployment, scaling, production operations |
| Official study guide | PDF / official guide | https://www.nvidia.com/en-eu/learn/certification/agentic-ai-professional/ | Exam blueprint and official topic coverage |

Note: NVIDIA course pricing can vary by region, account status, and promotional availability. Always verify the current course page before enrolling.

---

## 5. Free NVIDIA Resources to Use First

Use these before paid resources. They are enough to build a strong conceptual base.

| Resource | Link | What to Learn |
|---|---|---|
| NVIDIA Generative AI and LLM Learning Path | https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/ | Official learning path covering GenAI, RAG, NIM, deployment, and LLM application topics |
| Augment Your LLM Using Retrieval-Augmented Generation | https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/ | RAG fundamentals, retrieval, grounding, knowledge augmentation |
| Building RAG Agents With LLMs | https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/ | RAG agents, document retrieval, agentic retrieval patterns |
| Introduction to NVIDIA NIM Microservices | https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/ | NVIDIA inference microservices, deployment, API-based serving |
| NVIDIA NIM product overview | https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/ | What NIM is, why it matters, and where it fits in deployment |
| NVIDIA NIM documentation | https://docs.nvidia.com/nim/ | Hands-on details for deploying and using NIM microservices |
| NVIDIA NeMo documentation | https://docs.nvidia.com/nemo/ | NeMo suite, agent lifecycle, customization, evaluation, retrieval, guardrails |
| NVIDIA NeMo Guardrails docs | https://docs.nvidia.com/nemo-guardrails/ | Guardrails, safety policies, programmable rails, controlled LLM applications |
| NVIDIA NeMo Retriever docs | https://docs.nvidia.com/nemo/retriever/latest/ | Enterprise RAG, extraction, embeddings, indexing, reranking, retrieval microservices |
| NVIDIA API Catalog | https://build.nvidia.com/ | Explore hosted NVIDIA models, NIM APIs, blueprints, and example API usage |
| NVIDIA NGC Catalog | https://catalog.ngc.nvidia.com/ | Containers, models, Helm charts, and GPU-optimized software |
| NVIDIA Developer AI Agents topic page | https://developer.nvidia.com/topics/ai/ai-agents | AI agent concepts, examples, and NVIDIA ecosystem references |

---

## 6. NVIDIA-Specific Knowledge You Must Have

The exam includes a dedicated **NVIDIA Platform Implementation** domain and also expects NVIDIA-aware answers in deployment, scaling, evaluation, and safety scenarios.

| NVIDIA Area | What You Must Know | Where to Study |
|---|---|---|
| NVIDIA NIM | Optimized inference microservices, containerized deployment, OpenAI-compatible APIs, latency/throughput benefits, self-hosted vs hosted APIs | https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/ and https://docs.nvidia.com/nim/ |
| NVIDIA NeMo | Suite for building, customizing, evaluating, deploying, and optimizing AI agents and generative AI models | https://docs.nvidia.com/nemo/ |
| NeMo Framework | Training/customization framework for LLMs, multimodal, speech, and generative AI models; includes large-scale training and optimization concepts | https://docs.nvidia.com/nemo-framework/ |
| NeMo Retriever | RAG-oriented microservices for extraction, embeddings, indexing, semantic/hybrid search, reranking, and privacy-preserving enterprise retrieval | https://docs.nvidia.com/nemo/retriever/latest/ |
| NeMo Guardrails | Runtime guardrails for input/output controls, topic control, safety checks, programmable rails, and policy enforcement | https://docs.nvidia.com/nemo-guardrails/ |
| NeMo Evaluator | Evaluation and monitoring concepts such as benchmarking, LLM-as-judge, model and agent effectiveness | https://docs.nvidia.com/nemo/ |
| NVIDIA API Catalog | Hosted APIs to test models, agents, blueprints, and NIM endpoints without building full infrastructure first | https://build.nvidia.com/ |
| NVIDIA NGC | Catalog for containers, models, Helm charts, and GPU-optimized assets used in deployment workflows | https://catalog.ngc.nvidia.com/ |
| GPU inference concepts | Throughput, latency, batching, concurrency, quantization, model serving, and cost/performance tradeoffs | https://docs.nvidia.com/nim/ and https://docs.nvidia.com/nemo-framework/ |
| AI Blueprints | Reference architectures and examples for building AI applications and agents | https://build.nvidia.com/blueprints |

Exam-ready rule:

> If the question asks about production inference on NVIDIA infrastructure, think NIM. If it asks about agent lifecycle, customization, retrieval, evaluation, or guardrails, think NeMo and its related services.

---

## 7. 14-Day Preparation Plan

This plan assumes 2-3 hours on weekdays and 4-5 hours on weekends. If you have less time, keep the same order but reduce hands-on depth.

### Day 1 - Understand the Exam and Agentic AI Basics

Study:

- Official NCP-AAI certification page: https://www.nvidia.com/en-eu/learn/certification/agentic-ai-professional/
- NVIDIA AI Agents topic page: https://developer.nvidia.com/topics/ai/ai-agents
- NVIDIA Generative AI and LLM Learning Path overview: https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/

Focus:

- What agentic AI means
- Difference between chatbot, RAG assistant, and agent
- Exam domains and weights
- Agent lifecycle: plan, reason, act, observe, evaluate

Output:

- Create a one-page exam blueprint summary.

---

### Day 2 - RAG Fundamentals

Study:

- Augment Your LLM Using Retrieval-Augmented Generation: https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/
- NVIDIA NeMo Retriever overview: https://docs.nvidia.com/nemo/retriever/latest/

Focus:

- RAG pipeline: data source -> ingestion -> chunking -> embeddings -> vector DB -> retriever -> prompt -> LLM
- Grounding and hallucination reduction
- When to use RAG vs fine-tuning

Output:

- Draw a RAG architecture diagram and explain each component.

---

### Day 3 - Building RAG Agents

Study:

- Building RAG Agents With LLMs: https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-15+V1
- NeMo Retriever key concepts: https://docs.nvidia.com/nemo/retriever/latest/extraction/concepts/

Focus:

- Agentic RAG vs basic RAG
- Query routing
- Retrieval planning
- Multi-step retrieval
- Reranking
- Handling documents, tables, charts, and multimodal data

Output:

- Write 5 exam-style questions on RAG agents.

---

### Day 4 - Agent Architecture and Design

Study:

- Building Agentic AI Applications With LLMs: https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-18+V1
- NVIDIA AI Agents topic page: https://developer.nvidia.com/topics/ai/ai-agents

Focus:

- Planner-executor pattern
- Router agents
- Critic/evaluator agents
- Multi-agent collaboration
- Tool-using agents
- Agent communication and orchestration

Output:

- Create a table comparing single-agent, multi-agent, planner-executor, and router-agent patterns.

---

### Day 5 - Prompt Engineering and Agent Development

Study:

- Building LLM Applications With Prompt Engineering: https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/
- NVIDIA API Catalog examples: https://build.nvidia.com/

Focus:

- Prompt structure
- System vs user instructions
- Few-shot examples
- Tool/function calling
- Structured output
- Prompt constraints and failure handling

Output:

- Build a prompt template for a RAG agent that includes role, task, context, constraints, and output format.

---

### Day 6 - Cognition, Planning, and Memory

Study:

- Building Agentic AI Applications With LLMs: https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-18+V1
- NeMo documentation landing page: https://docs.nvidia.com/nemo/

Focus:

- Reasoning strategies
- Task decomposition
- Short-term memory
- Long-term memory
- Episodic, semantic, and procedural memory
- Planning failures and recovery strategies

Output:

- Create a memory comparison table: conversation memory, vector memory, tool state, persistent user profile.

---

### Day 7 - Evaluation and Semantic Search

Study:

- Evaluating RAG and Semantic Search Systems: https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-16+V1
- NeMo Evaluator area: https://docs.nvidia.com/nemo/

Focus:

- Retrieval metrics: precision@k, recall@k, MRR, nDCG, hit rate
- Generation metrics: faithfulness, groundedness, answer relevance, context relevance
- Agent metrics: tool success rate, task completion rate, plan quality, step failure rate
- LLM-as-judge evaluation

Output:

- Create an evaluation cheat sheet with metric definitions and when to use each metric.

---

### Day 8 - NVIDIA NIM and Inference Deployment

Study:

- Introduction to NVIDIA NIM Microservices: https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/
- NVIDIA NIM product page: https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/
- NVIDIA NIM docs: https://docs.nvidia.com/nim/

Focus:

- NIM as optimized inference microservices
- Hosted API vs self-hosted deployment
- Containers and APIs
- Throughput, latency, concurrency, batching
- Scaling inference for agentic applications

Output:

- Write a short explanation: where NIM fits in an agentic RAG architecture.

---

### Day 9 - NeMo, Retriever, and Enterprise RAG

Study:

- NVIDIA NeMo docs: https://docs.nvidia.com/nemo/
- NeMo Retriever latest docs: https://docs.nvidia.com/nemo/retriever/latest/
- NeMo Retriever extraction overview: https://docs.nvidia.com/nemo/retriever/latest/extraction/overview/

Focus:

- NeMo suite purpose
- Retrieval pipelines
- Extraction and ingestion
- Embedding, indexing, semantic search, hybrid search, reranking
- Privacy-preserving retrieval for enterprise data

Output:

- Map a basic RAG pipeline to NVIDIA components: NeMo Retriever, NIM, vector database, LLM endpoint.

---

### Day 10 - Guardrails, Safety, Ethics, and Compliance

Study:

- NeMo Guardrails docs: https://docs.nvidia.com/nemo-guardrails/
- NeMo Guardrails platform docs: https://docs.nvidia.com/nemo/microservices/latest/guardrails/index.html

Focus:

- Input guardrails
- Output guardrails
- Retrieval guardrails
- Tool/action guardrails
- Topic control
- Policy enforcement
- Human approval for high-impact actions

Output:

- Create a guardrail matrix: risk scenario -> control -> example.

---

### Day 11 - Deployment, Scaling, Monitoring, and Maintenance

Study:

- Introduction to Deploying RAG Pipelines for Production at Scale: https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-17+V1
- NVIDIA NIM docs: https://docs.nvidia.com/nim/
- NGC Catalog: https://catalog.ngc.nvidia.com/

Focus:

- Production RAG deployment
- Scaling retrievers and LLM inference
- Monitoring latency, cost, throughput, failure rate, retrieval quality
- Logs, traces, metrics, alerts
- Rollback and versioning

Output:

- Create a production readiness checklist for a RAG agent.

---

### Day 12 - Adding New Knowledge to LLMs

Study:

- Adding New Knowledge to LLMs: https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-14+V1
- NeMo Framework docs: https://docs.nvidia.com/nemo-framework/
- NeMo Customizer area: https://docs.nvidia.com/nemo/

Focus:

- RAG vs fine-tuning vs prompt engineering
- When to update the knowledge base
- When to customize or fine-tune
- Knowledge freshness and governance
- Domain-specific data handling

Output:

- Create a decision table: RAG vs fine-tuning vs prompt engineering vs larger model.

---

### Day 13 - Hands-On Mini Project

Build:

- A small RAG or agentic RAG prototype using any accessible tools.
- Use NVIDIA API Catalog if available: https://build.nvidia.com/
- Reference NIM docs for how production inference would work: https://docs.nvidia.com/nim/
- Reference NeMo Retriever for how enterprise retrieval would work: https://docs.nvidia.com/nemo/retriever/latest/
- Reference NeMo Guardrails for safety layer design: https://docs.nvidia.com/nemo-guardrails/

Minimum architecture:

1. Data source: 3-5 Markdown/PDF/text documents
2. Ingestion: split into chunks
3. Embeddings: create searchable vectors
4. Retrieval: top-k search
5. Generation: answer using retrieved context
6. Evaluation: check groundedness and answer relevance
7. Guardrails: refuse unsupported answers or risky actions

Output:

- Architecture diagram
- README
- Validation tests
- Lessons learned

---

### Day 14 - Final Review and Weak-Area Repair

Study:

- Official certification page and blueprint: https://www.nvidia.com/en-eu/learn/certification/agentic-ai-professional/
- NVIDIA learning path: https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/
- NeMo docs: https://docs.nvidia.com/nemo/
- NIM docs: https://docs.nvidia.com/nim/
- NeMo Guardrails docs: https://docs.nvidia.com/nemo-guardrails/

Focus:

- Review all exam domains
- Redo weak topics
- Memorize product mapping
- Review RAG metrics and guardrails
- Review agent design patterns

Output:

- Final 2-page cheat sheet.

---

## 8. One-Week Practice Plan

Use the final week for practice, not for starting new deep courses.

| Day | Task | Output |
|---|---|---|
| Practice Day 1 | Take first timed mock exam or 60 mixed questions | Score by domain |
| Practice Day 2 | Review all wrong answers | Weak-topic list |
| Practice Day 3 | Take second timed mock exam | Compare score and timing |
| Practice Day 4 | Deep review of RAG, evaluation, deployment, NVIDIA products | Updated cheat sheet |
| Practice Day 5 | Take third timed mock exam | Target 80%+ |
| Practice Day 6 | Redo missed questions only | Final weak-area repair |
| Practice Day 7 | Light review only | Rest, logistics, confidence |

Practice exam rule:

> Do not just memorize answers. For every missed question, identify the domain, the concept, the trap, and the correct decision rule.

---

## 9. Where to Learn Practice Questions From

NVIDIA may not provide a large public free question bank for this certification. Build practice using official objectives and reputable sources.

| Source | Link | How to Use It |
|---|---|---|
| Official NVIDIA certification page | https://www.nvidia.com/en-eu/learn/certification/agentic-ai-professional/ | Convert every exam domain and topic into flashcards and scenario questions |
| Official NVIDIA study guide | Linked from the certification page under Exam Study Guide | Use it as the source of truth for objectives and terminology |
| NVIDIA recommended courses | See Section 4 | Turn end-of-module concepts into questions |
| NVIDIA Generative AI learning path | https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/ | Use course summaries and labs to create review questions |
| NVIDIA Docs | https://docs.nvidia.com/ | Write product-specific questions on NIM, NeMo, Retriever, Guardrails, NGC |
| NVIDIA API Catalog | https://build.nvidia.com/ | Practice identifying where hosted APIs, blueprints, and NIM endpoints fit |
| NVIDIA Developer forums | https://forums.developer.nvidia.com/ | Read real troubleshooting and deployment discussions |
| Your own mini project | Local GitHub repo | Convert every design choice and bug into a question |

Recommended self-made question categories:

- Scenario-based architecture questions
- RAG troubleshooting questions
- Evaluation metric selection questions
- Deployment and scaling tradeoff questions
- Guardrail and human oversight questions
- NVIDIA product mapping questions

Example practice-question prompt to generate your own review set:

```text
Create 20 scenario-based practice questions for the NVIDIA NCP-AAI exam.
Cover: RAG, agent architecture, tool use, memory, evaluation, deployment, NIM, NeMo Retriever, NeMo Guardrails, and human oversight.
For each question, include 4 options, the correct answer, and a detailed explanation.
Avoid answer patterns and avoid trivia-only questions.
```

Avoid relying on exam dumps. They may be inaccurate, unethical, outdated, and can violate exam policies.

---

## 10. Exam Traps to Watch For

| Trap | Wrong Instinct | Better Exam Answer | Study Link |
|---|---|---|---|
| Dynamic domain data | Fine-tune every time documents change | Use RAG and update the knowledge/index | https://docs.nvidia.com/nemo/retriever/latest/ |
| Unsupported answers | Increase temperature | Improve retrieval, grounding, citations, and faithfulness evaluation | https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-16+V1 |
| Slow production RAG | Only change prompt | Investigate latency, batching, retrieval, reranking, model serving, and NIM deployment | https://docs.nvidia.com/nim/ |
| Poor retrieval quality | Use a larger LLM only | Fix chunking, embeddings, top-k, hybrid search, reranking, metadata filtering | https://docs.nvidia.com/nemo/retriever/latest/extraction/concepts/ |
| Risky tool actions | Let agent act autonomously | Add human approval, tool permissioning, audit logs, and action guardrails | https://docs.nvidia.com/nemo-guardrails/ |
| Need company tone | Use RAG only | Prompt engineering or fine-tuning may be better for behavior/style | https://docs.nvidia.com/nemo-framework/ |
| Need latest internal facts | Fine-tune the model | Use RAG/NeMo Retriever for external knowledge | https://docs.nvidia.com/nemo/retriever/latest/ |
| Need production inference | Manually host ad hoc model server | Use NIM for optimized inference microservices | https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/ |
| Need safety controls | Rely only on prompt instructions | Use guardrails, policy checks, moderation, and HITL | https://docs.nvidia.com/nemo/microservices/latest/guardrails/index.html |
| Agent failure debugging | Look only at final answer | Inspect traces, tool calls, retrieval results, intermediate steps, and logs | https://docs.nvidia.com/nemo/ |

High-yield rules:

- RAG is for knowledge.
- Fine-tuning is for behavior or task specialization.
- Prompt engineering is the fastest low-cost optimization.
- NIM is for optimized inference deployment.
- NeMo Retriever is for enterprise RAG pipelines.
- NeMo Guardrails is for safety, policy, and controllability.
- Evaluation must cover retrieval, generation, agent behavior, safety, latency, and cost.

---

## 11. Final Readiness Checklist

Use this checklist before starting practice-exam week.

### Agent Architecture and Design

- [ ] I can explain agent loop: observe -> reason/plan -> act -> observe.
- [ ] I can compare single-agent, multi-agent, router, planner-executor, and critic patterns.
- [ ] I know when to use human-in-the-loop approval.
- [ ] I can identify failure points in multi-agent workflows.

Study links:

- https://developer.nvidia.com/topics/ai/ai-agents
- https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-18+V1

### Agent Development

- [ ] I understand tool calling and function calling.
- [ ] I can design prompts with clear role, task, context, constraints, and output format.
- [ ] I can explain structured output and validation.
- [ ] I can describe how agents handle tool failures.

Study links:

- https://build.nvidia.com/
- https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/

### RAG and Knowledge Integration

- [ ] I can draw a RAG architecture from memory.
- [ ] I understand chunking, embeddings, vector databases, retrievers, rerankers, and prompt builders.
- [ ] I know semantic vs keyword vs hybrid search.
- [ ] I can explain RAG vs fine-tuning.

Study links:

- https://docs.nvidia.com/nemo/retriever/latest/
- https://docs.nvidia.com/nemo/retriever/latest/extraction/concepts/

### Evaluation and Tuning

- [ ] I know precision@k, recall@k, MRR, nDCG, hit rate.
- [ ] I know faithfulness, groundedness, answer relevance, and context relevance.
- [ ] I can explain LLM-as-judge and its risks.
- [ ] I can evaluate agent tool success and task completion.

Study links:

- https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-16+V1
- https://docs.nvidia.com/nemo/

### Deployment and Scaling

- [ ] I know how latency, throughput, batching, concurrency, and cost interact.
- [ ] I can explain where NIM fits in production inference.
- [ ] I know what should be monitored in production RAG and agent systems.
- [ ] I can describe rollback/versioning for prompts, models, indexes, and tools.

Study links:

- https://docs.nvidia.com/nim/
- https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/
- https://catalog.ngc.nvidia.com/

### NVIDIA Platform Implementation

- [ ] I can map NIM, NeMo, NeMo Retriever, NeMo Guardrails, API Catalog, and NGC to use cases.
- [ ] I know the difference between hosted APIs and self-hosted NIM.
- [ ] I can explain how NVIDIA tools support production agentic AI.

Study links:

- https://docs.nvidia.com/nemo/
- https://docs.nvidia.com/nim/
- https://build.nvidia.com/
- https://catalog.ngc.nvidia.com/

### Safety, Ethics, Compliance, and Oversight

- [ ] I understand input, output, retrieval, and tool/action guardrails.
- [ ] I can identify when to use HITL.
- [ ] I understand audit logs, access controls, and data minimization.
- [ ] I can explain how to handle unsupported answers.

Study links:

- https://docs.nvidia.com/nemo-guardrails/
- https://docs.nvidia.com/nemo/microservices/latest/guardrails/index.html

---

## 12. Quick NVIDIA Product Mapping

| Exam Scenario | NVIDIA Product / Resource | Why |
|---|---|---|
| Need optimized LLM inference as an API | NVIDIA NIM | Prebuilt optimized inference microservices |
| Need to test hosted models quickly | NVIDIA API Catalog | Hosted model/API experimentation |
| Need self-hosted production model serving | NVIDIA NIM + NGC containers | Deployable microservices and containers |
| Need enterprise RAG over documents | NeMo Retriever | Extraction, embedding, indexing, retrieval, reranking |
| Need to process PDFs, tables, charts, infographics | NeMo Retriever Extraction / NVIDIA Ingest | Multimodal document extraction and metadata processing |
| Need safety and policy controls | NeMo Guardrails | Programmable input/output/topic/tool guardrails |
| Need to customize or train generative models | NeMo Framework / NeMo Customizer | Model customization and training workflows |
| Need to evaluate models or agents | NeMo Evaluator | Benchmarking and effectiveness evaluation |
| Need containers, models, Helm charts | NVIDIA NGC Catalog | GPU-optimized deployment assets |
| Need reference architectures | NVIDIA AI Blueprints | Starting points for production-style applications |
| Need model optimization concepts | NeMo Framework docs | Parallelism, quantization, distillation, MoE, large-scale training |

Links:

- NIM: https://docs.nvidia.com/nim/
- NIM product page: https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/
- NeMo: https://docs.nvidia.com/nemo/
- NeMo Framework: https://docs.nvidia.com/nemo-framework/
- NeMo Retriever: https://docs.nvidia.com/nemo/retriever/latest/
- NeMo Guardrails: https://docs.nvidia.com/nemo-guardrails/
- API Catalog: https://build.nvidia.com/
- AI Blueprints: https://build.nvidia.com/blueprints
- NGC Catalog: https://catalog.ngc.nvidia.com/

---

## 13. Suggested Hands-On Mini Project

Build this project to connect multiple exam domains:

# Agentic RAG Assistant With Evaluation and Guardrails

## Objective

Build a small agentic RAG assistant that answers questions from a controlled document set, evaluates retrieval and answer quality, and applies safety/grounding rules before returning the final answer.

## Architecture

```text
User Question
    |
    v
Router / Planner Agent
    |
    v
Retriever
    |
    v
Optional Reranker
    |
    v
Prompt Builder
    |
    v
LLM / NIM Endpoint or Local LLM
    |
    v
Evaluator / Critic
    |
    v
Guardrails
    |
    v
Final Answer With Sources
```

## Minimum Features

| Feature | Exam Domain Covered | Reference |
|---|---|---|
| Document ingestion and chunking | Knowledge Integration | https://docs.nvidia.com/nemo/retriever/latest/extraction/concepts/ |
| Embeddings and vector search | Knowledge Integration | https://docs.nvidia.com/nemo/retriever/latest/ |
| Reranking or metadata filtering | Evaluation and RAG tuning | https://docs.nvidia.com/nemo/retriever/latest/ |
| Prompt builder with constraints | Agent Development | https://www.nvidia.com/en-us/learn/learning-path/generative-ai-llm/ |
| Tool-use or router logic | Agent Architecture | https://developer.nvidia.com/topics/ai/ai-agents |
| Evaluation metrics | Evaluation and Tuning | https://learn.nvidia.com/courses/course-detail?course_id=course-v1:DLI+S-FX-16+V1 |
| Guardrails for unsupported answers | Safety and Compliance | https://docs.nvidia.com/nemo-guardrails/ |
| Production deployment design | Deployment and Scaling | https://docs.nvidia.com/nim/ |

## Suggested Repository Structure

```text
agentic-rag-evaluation-guardrails-poc/
|
├── README.md
├── architecture/
│   └── rag-agent-architecture.png
├── data/
│   └── sample-documents/
├── src/
│   ├── ingest.py
│   ├── retrieve.py
│   ├── generate.py
│   ├── evaluate.py
│   └── guardrails.py
├── prompts/
│   └── rag-agent-prompt.md
├── evaluations/
│   ├── test-questions.md
│   └── evaluation-results.md
├── docs/
│   ├── design-decisions.md
│   ├── troubleshooting.md
│   └── exam-domain-mapping.md
└── requirements.txt
```

## Validation Tests

- Ask a question that is answered in the documents.
- Ask a question that is not in the documents and verify the assistant refuses to invent an answer.
- Change chunk size and compare retrieval quality.
- Test top-k values and observe precision/recall tradeoff.
- Add a risky request and verify guardrails block or escalate it.
- Compare answers with and without reranking.
- Record latency and token usage for each request.

## Portfolio README Points

Include these in the project README:

- Problem statement
- Architecture diagram
- Tools used
- RAG pipeline explanation
- Agent workflow explanation
- Evaluation metrics
- Guardrail rules
- Sample prompts and outputs
- Known limitations
- Future improvements using NVIDIA NIM, NeMo Retriever, and NeMo Guardrails

## Optional NVIDIA Alignment

If you have access to NVIDIA-hosted APIs or infrastructure:

- Use NVIDIA API Catalog for hosted model testing: https://build.nvidia.com/
- Use NIM concepts for production inference design: https://docs.nvidia.com/nim/
- Reference NeMo Retriever for enterprise retrieval design: https://docs.nvidia.com/nemo/retriever/latest/
- Reference NeMo Guardrails for policy enforcement design: https://docs.nvidia.com/nemo-guardrails/

---

## 14. Final Study Strategy

Prioritize in this order:

1. RAG and knowledge integration
2. Agent architecture and tool use
3. Evaluation and tuning
4. Deployment and scaling
5. Planning, memory, and cognition
6. NVIDIA platform mapping
7. Guardrails, compliance, and human oversight

Final exam mindset:

> Choose the answer that produces a reliable, grounded, observable, scalable, and safe agentic AI system, not merely the answer that makes the model more powerful.

