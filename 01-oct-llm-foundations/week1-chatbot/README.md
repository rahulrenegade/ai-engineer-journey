# Week 1 — "The Goldfish Problem" 🐟

**Mission:** Build a terminal chatbot with memory, then break its memory on purpose.
**Time:** ~5 hrs main quest + ~1–2 hrs side quest
**Rule:** You write the code. Claude explains, hints, and reviews, but doesn't write it for you.

---

## The big secret of this week
> **An LLM has no memory.** Every call starts from zero.
> A chatbot "remembers" only because *your code* sends the whole conversation again on every turn.

Once you really understand this, context windows, cost, RAG and agents all start to make sense.

---

## Concepts (read first, ~30 min)

**1. Messages and roles.** You send the model a list of messages:
```python
[
  {"role": "system",    "content": "You are a sarcastic pirate."},     # rules and persona
  {"role": "user",      "content": "What's 2+2?"},                    # you
  {"role": "assistant", "content": "4, ye landlubber."},              # the model's earlier reply
  {"role": "user",      "content": "Times 10?"},                      # the new question
]
```
The model only sees this list. To answer "Times 10?", it needs the earlier turns in the list.

**2. Tokens.** The model reads and writes *tokens* (pieces of words), not words.
Ollama tells you how many were used on every response:
- `prompt_eval_count` = tokens you sent in (input)
- `eval_count` = tokens it generated (output)

**3. Context window.** The maximum number of tokens the model can see at once (input + output).
When the conversation gets bigger than the window, the oldest content gets **silently dropped**. That's the goldfish moment.

**4. Temperature.** The model predicts a probability for every possible next token, then *samples* one.
- `temperature=0` → almost always picks the top token (repeatable, boring)
- `temperature=1.5` → picks riskier tokens (creative, then chaotic)

---

## Levels

### Level 1: First contact (`ask.py`), ~45 min
A script that takes a question from the command line and prints the answer.
```bash
uv run python week1-chatbot/ask.py "Why is the sky blue?"
```
**Requirements:**
- Use `ollama.chat(...)` with a single user message
- After the answer, print: input tokens, output tokens, and time taken (seconds)

💡 *Hint:* the response object has `prompt_eval_count`, `eval_count` and `total_duration` (in nanoseconds).

### Level 2: The chatbot (`chat.py`), ~1.5 hrs
An interactive loop: you type, it answers, and it **remembers** the conversation.
**Requirements:**
- A `messages` list that grows each turn (append the user message *and* the assistant reply)
- A system prompt that gives it a personality of your choice
- Commands: `/exit` to quit, `/reset` to clear memory (but keep the system prompt), `/tokens` to show the last input token count
- **Streaming:** print the reply word by word as it's generated (`stream=True`)

✅ *Test:* tell it your name, chat for 3 turns, then ask "what's my name?"
👀 *Watch:* `/tokens` keeps going up every turn. Why?

### Level 3: The temperature lab (`temperature_lab.py`), ~45 min
Send the **same prompt** 3 times at each of `temperature` = 0, 0.7 and 1.5.
Prompt idea: *"Invent a name for a new coffee shop. Reply with only the name."*
Write what you observe in `NOTES.md`.

💡 *Hint:* `options={"temperature": 0.7}`

### Level 4: Break it 🔨 (back in `chat.py`), ~1 hr
Shrink the context window: `options={"num_ctx": 512}`.
1. Tell the bot: *"The secret password is PINEAPPLE-42. Remember it."*
2. Paste in a few long paragraphs (any article) over several turns
3. Ask: *"What's the secret password?"*

It forgets. Watch `/tokens`. Does it stop growing at some point? Why?

**Now fix it:** add trimming to your code, so that when the conversation gets too long, *you* decide what to drop, not Ollama.
- Always keep the system prompt
- Keep the most recent N messages (or stay under a token budget)
- Stretch goal: keep "important" messages pinned

### Level 5 (bonus): Two brains
- Add `--provider gemini` so the same chatbot can use Gemini instead of Ollama
- Gemini sometimes returns `503` (you've seen it already). Add **retry with exponential backoff** (wait 1s, 2s, 4s…)
- Compare: how does the 3B local model differ from Gemini on the same questions?

---

## Side quest: micrograd (part 1)
Watch Karpathy's **"The spelled-out intro to neural networks and backpropagation: building micrograd"** (YouTube), up to about the 1-hour mark.
Code along in `side-quest-build-llm/01-micrograd/`. Don't copy and paste; type it out yourself.

---

## Done when
- [ ] `ask.py`, `chat.py`, `temperature_lab.py` work
- [ ] You broke the memory and fixed it with trimming
- [ ] `NOTES.md` written: what you built, what surprised you, what broke
- [ ] 3–5 lines added to `notes/concepts.md` for tokens, context window and temperature
- [ ] Committed and pushed
- [ ] **Boss quiz:** tell Claude "quiz me on week 1"
