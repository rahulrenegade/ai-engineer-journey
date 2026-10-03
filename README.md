# AI Journey — Rahul Mullaguru

From Application Engineer → AI Engineer. Deadline: **May 2027** (Toronto). Checkpoint: **70–80% ready by Feb 2027**.

## How this folder is organized

```
AI-Journey/
├── README.md                  ← you are here (map + rules)
├── PROGRESS.md                ← checklist; tick things off as you go
├── 00-setup/SETUP.md          ← START HERE: install everything step by step
├── 01-oct-llm-foundations/    ← Month 1: tokens, prompts, structured output, tool calling
│   ├── week1-chatbot/
│   ├── week2-invoice-extractor/
│   ├── week3-tool-calling/
│   └── week4-embeddings/
├── 02-nov-rag/                ← Month 2: FinRAG v1 (the real RAG project)
├── 03-dec-evals-agents/       ← Month 3: evals + agents + MCP (PipelineDoctor)
├── 04-jan-production/         ← Month 4: deploy on AWS, observability, resume
├── 05-feb-finetuning/         ← Month 5: LoRA/QLoRA, start applying
├── 06-mar-system-design/      ← Month 6: AI system design + mocks
├── 07-apr-capstone/           ← Month 7: capstone
├── 08-may-final/              ← Month 8: interviews + buffer
├── side-quest-build-llm/      ← build an LLM from scratch, step by step
│   ├── 01-micrograd/  02-makemore/  03-build-gpt/  04-tokenizer/
│   └── 05-my-own-gpt/  06-inference/  07-gpt2-repro/
├── interview-prep/            ← dsa/, system-design/, behavioral/
└── notes/                     ← concepts.md: your own explanations in your own words
```

## Rules
1. **One month = one folder = one Python project** (its own `pyproject.toml` + `.venv`). Never install packages globally.
2. **Every week folder gets a short `NOTES.md`**: what I built, what broke, what I learned.
3. **Secrets live only in `.env`** (already git-ignored). Never paste API keys into code.
4. **Commit at the end of every session.** Small commits, clear messages.
5. **Explain it back.** After each week, write 3–5 lines in `notes/concepts.md` in your own words.

## Weekly rhythm (5–8 hrs)
- ~5 hrs main quest (the week's build)
- ~1–3 hrs side quest (build-your-own-LLM)
- End of week: quiz with Claude → update PROGRESS.md → commit
