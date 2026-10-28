# HANDOVER — October: LLM Foundations

> ↑ Back to [index](../../HANDOVER.md). Last updated: 2026-10-28

## Month goal
Reliable structured output and tool calling, as the base for RAG and agents. Spec per week lives in each week's `README.md`.

| Week | Folder | Status |
|---|---|---|
| 1 — The Goldfish Problem (chatbot + memory) | `week1-chatbot/` | 🟡 in progress (L3 of 5) |
| 2 — Invoice extractor (structured output) | `week2-invoice-extractor/` | ⬜ not started (folder not created) |
| 3 — Tool calling from scratch | `week3-tool-calling/` | ⬜ not started |
| 4 — Embeddings + semantic search | `week4-embeddings/` | ⬜ not started |
| Side quest — micrograd | `../side-quest-build-llm/01-micrograd/` | ⬜ not started (empty) |

## Week 1 detail (`week1-chatbot/`)
| Level | File | Status | Open items |
|---|---|---|---|
| L1 one-shot call | `ask.py` | ✅ done | Nit: stale comments on lines 7–8 ("the model's earlier reply") |
| L2 chatbot | `chat.py` | ✅ done, committed `fd2db10` | Nit: `print(GREETINGS)` sits between constants and the function; move it above `while True` |
| L3 temperature lab | `temperature_lab.py` | 🟡 runs 3× per temperature; **untracked** | (1) remove the witty `SYSTEM_PROMPT` so only temperature varies (one-variable experiment); (2) print a newline after each row / drop the trailing ` \| `; (3) fill in the NOTES.md table and "what I noticed"; (4) write the temperature concept in `notes/concepts.md` |
| L4 break and fix memory | `chat.py` | ⬜ | `num_ctx: 512`, password test, then trimming that keeps the system prompt plus the last N messages |
| L5 Gemini + retries | — | ⬜ bonus | `--provider gemini`, exponential backoff for 503s. Suggested refactor: shared `llm.py` used by `ask.py` and `chat.py` |

`NOTES.md` is still an empty template. `PROGRESS.md` has no boxes ticked yet (setup is actually done, so tick those).

## What Rahul has learned (don't re-teach; build on it)
- LLMs are stateless: memory = resending the `messages` list. Roles matter (he hit the system-vs-assistant role bug).
- Chat templates and special tokens: why "my name is rahul" cost 31 input tokens (from `ollama show llama3.2:3b --template`).
- `prompt_eval_count` is already cumulative, so don't sum it; keep stats out of `messages`.
- Streaming = generator; print the new piece and accumulate the full reply (he hit both versions of this bug).
- Loop control-flow debugging (the `/reset` infinite loop); the habit of a `new_conversation()` helper to avoid duplication.
- 128 input tokens after 3 turns: context grows every turn.

## Not yet covered (upcoming)
Context-window overflow and trimming (L4), provider abstraction and retries (L5), structured output with Pydantic (W2), tool calling (W3), embeddings (W4), backprop (micrograd).
