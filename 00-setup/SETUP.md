# Setup — step by step

Do these in order. Each step says **what**, **why**, the **command**, and how to **verify** it worked.
Tick each one off in `PROGRESS.md`. Total time: ~45–60 min (mostly downloads).

---

## Step 0 — Open the terminal in the right place
```bash
cd ~/Desktop/AI-Journey
```
Every command below assumes you start here unless it says otherwise.

---

## Step 1 — Turn off Anaconda's auto-activation
**Why:** Your Mac's `python3` currently points at Anaconda (`/opt/anaconda3`). If both Anaconda and uv manage Python, you'll get confusing "module not found" errors. We'll let **uv** own all projects here. Anaconda stays installed — you can still use it on demand with `conda activate base`.

```bash
conda config --set auto_activate_base false
```
Now **close and reopen the terminal**.

**Verify:** your prompt no longer starts with `(base)`.

---

## Step 2 — Install uv (your Python manager)
**Why:** `uv` replaces `pip` + `venv` + `pyenv` in one fast tool. It's the modern standard and what you'll see in most new AI repos.

```bash
brew install uv
```
**Verify:**
```bash
uv --version
```

---

## Step 3 — Install Python 3.12 via uv
**Why:** 3.12 is the sweet spot — every major AI library (PyTorch, transformers, etc.) supports it. 3.13 still has occasional gaps.

```bash
uv python install 3.12
```
**Verify:**
```bash
uv python list --only-installed
```

---

## Step 4 — Install Ollama (run LLMs locally, for free)
**Why:** You get unlimited free experiments on your own Mac, and you learn what a model really is — a file you download and run.

```bash
brew install ollama
brew services start ollama      # runs Ollama in the background, starts on login
ollama pull llama3.2:3b         # ~2 GB download
```
**Verify:**
```bash
ollama run llama3.2:3b "Explain a token in one sentence"
```
You should get an answer in a few seconds.

**Useful Ollama commands:**
| Command | What it does |
|---|---|
| `ollama list` | models you've downloaded |
| `ollama ps` | models currently loaded in memory |
| `ollama stop llama3.2:3b` | unload a model and free your RAM |
| `ollama rm <model>` | delete a model and free disk space |

**8 GB RAM tip:** close heavy Chrome tabs when running models. Stick to models of **3B parameters or less** for now.

---

## Step 5 — Get a free Gemini API key (cloud model)
**Why:** Local 3B models are small. A free cloud model lets you compare a small model with a strong one, which teaches you a lot.

1. Go to https://aistudio.google.com → **Get API key** → **Create API key**.
2. Copy the key. You'll paste it in Step 7.
3. Note which free model is listed (for example `gemini-3.1-flash-lite`). If it's different, use that name in `.env`.

---

## Step 6 — Set up Git (do this before creating projects)
**Why:** Version control from day 1 means every session is saved and backed up, and your progress shows on your GitHub.

```bash
git config --global user.name    # check: should print your name
git config --global user.email   # check: should print your email
# if either is empty:
git config --global user.name "Rahul Mullaguru"
git config --global user.email "you@example.com"

git init
git add .
git commit -m "Initial structure: roadmap, progress tracker, setup guide"
```
**Verify:** `git log --oneline` shows 1 commit.

**Push to GitHub:**
1. github.com → **New repository** → name it `ai-engineer-journey` → **Public** → do **not** add a README (you already have one).
2. Then run:
```bash
git branch -M main
git remote add origin https://github.com/rahulrenegade/ai-engineer-journey.git
git push -u origin main
```
If it asks for a password, use a **Personal Access Token** (GitHub → Settings → Developer settings → Tokens), or install the GitHub CLI with `brew install gh` and run `gh auth login`.

---

## Step 7 — Create the October project
**Why:** Each month is its own isolated Python project with its own packages, so nothing ever conflicts.

```bash
cd 01-oct-llm-foundations
uv init --bare --python 3.12           # creates pyproject.toml only
uv add ollama google-genai pydantic python-dotenv
cp ../00-setup/.env.example .env       # then open .env and paste your Gemini key
```

**What just happened:**
| File / folder | What it is |
|---|---|
| `pyproject.toml` | your project's list of dependencies (committed to git) |
| `uv.lock` | the exact versions installed, so the setup can be reproduced (committed) |
| `.venv/` | the actual installed packages (git-ignored, can be recreated any time) |
| `.env` | your secrets (git-ignored) |

**Golden rule:** run Python with `uv run`. It always uses this project's `.venv`.
```bash
uv run python some_file.py
```

---

## Step 8 — Smoke test: both models answer
```bash
# still inside 01-oct-llm-foundations/
uv run ../00-setup/smoke_test.py
```
**Expected:**
```
[OK] Ollama (llama3.2:3b): A token is ...
[OK] Gemini (gemini-3.1-flash-lite): A token is ...
```
If you see `[FAIL]`, check Troubleshooting below.

---

## Step 9 — VS Code
```bash
code --install-extension ms-python.python
code --install-extension charliermarsh.ruff
code --install-extension ms-toolsai.jupyter
code ~/Desktop/AI-Journey
```
In VS Code: press `Cmd+Shift+P` → **Python: Select Interpreter** → choose `01-oct-llm-foundations/.venv`.

---

## Step 10 — Commit
```bash
cd ~/Desktop/AI-Journey
git add .
git status        # make sure .env is NOT listed!
git commit -m "Setup complete: uv, Ollama, Gemini, October project"
git push
```

✅ **Setup done.** Tick everything in `PROGRESS.md` and tell Claude: *"setup done, start week 1"*.

---

## Cheat sheet
| I want to... | Command |
|---|---|
| add a package | `uv add <pkg>` |
| remove a package | `uv remove <pkg>` |
| run a script | `uv run python file.py` |
| rebuild the env from scratch | `rm -rf .venv && uv sync` |
| see the installed packages | `uv pip list` |
| save my work | `git add . && git commit -m "msg" && git push` |

## Troubleshooting
| Problem | Fix |
|---|---|
| `[FAIL] test_ollama ... connection refused` | Ollama isn't running: `brew services start ollama` |
| `model not found` | `ollama pull llama3.2:3b` |
| Gemini `404 model not found` | change `GEMINI_MODEL` in `.env` to the model name shown in AI Studio |
| Gemini `429` | free-tier rate limit; wait a minute |
| Mac is very slow | `ollama stop llama3.2:3b`, close Chrome tabs |
| `(base)` still in the prompt | you didn't reopen the terminal after Step 1 |
| `.env` shows up in `git status` | stop! Check that `.gitignore` is in the AI-Journey root |
