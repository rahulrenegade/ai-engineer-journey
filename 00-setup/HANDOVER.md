# HANDOVER — Environment & Setup

> ↑ Back to [index](../../HANDOVER.md). Last updated: 2026-10-28. Full install steps: [SETUP.md](SETUP.md).

## Current setup (all done and working)
- **uv** manages Python. Global config `~/.config/uv/uv.toml` has `python-preference = "only-managed"`, so uv ignores the 7+ other Pythons on this Mac (Anaconda 3.13, Homebrew 3.14, python.org 3.12.4, …).
- **Per-month project:** each month folder has its own `pyproject.toml`, `uv.lock`, `.python-version` (3.12) and `.venv`. October deps: `ollama`, `google-genai`, `pydantic`, `python-dotenv`.
- **Anaconda** is installed at `/opt/anaconda3`; auto-activate is off.
- **Ollama** runs as a brew service; model `llama3.2:3b`.
- **Gemini:** free AI Studio key; billing off. Rahul also has a Google AI Pro subscription (consumer plan, doesn't cover the API, renews Dec 5; suggested cancelling to free up his $20/mo).
- **Git:** SSH key `~/.ssh/id_ed25519` added to GitHub.
- **VS Code:** `.vscode/settings.json` (git-ignored by Rahul's choice) sets the interpreter to the October `.venv` and disables the Python Environments extension.

## Issues already hit, and their fixes
| Symptom | Cause | Fix |
|---|---|---|
| `.venv` used Anaconda 3.13 | `requires-python >=3.12` let uv pick Anaconda | uv `only-managed` config + `uv python pin 3.12`, rebuild `.venv` |
| `ModuleNotFoundError: ollama` | ran plain `python`, or from the wrong folder | `uv run python …` from the month folder |
| VS Code "Failed to resolve env" / venv not listed | `.venv` is one level down; Python Environments extension; `~` not expanded | settings.json above; or open the month folder directly; use an absolute path |
| `REMOTE HOST IDENTIFICATION HAS CHANGED` (github.com) | old 2023 GitHub RSA host key in known_hosts | replaced with keys from `api.github.com/meta` (backup: `known_hosts.old`) |
| `Permission denied (publickey)` | old `id_rsa` not on GitHub | new ed25519 key |
| Push rejected (non-fast-forward) | local `.git` re-initialized | `git reset --soft origin/main`, then commit |
| Smoke test: GEMINI key not found | `load_dotenv()` searched from the script's folder | `find_dotenv(usecwd=True)` |
| Gemini AFC warning | SDK default | `AutomaticFunctionCallingConfig(disable=True)` |
| Gemini `503 UNAVAILABLE` | Google-side load | retry later; Week 1 L5 adds backoff |

## Security notes
- An API key was once committed locally; the commit was amended **before** reaching GitHub. Remote history verified clean.
- `../Gemini API Key Details/` (next to the repo, **outside** it) holds the key as .rtf/.png. Never move it into the repo.

## New month checklist
`cd <month-folder> && uv init --bare --python 3.12 && uv python pin 3.12 && uv add <deps>`, copy `.env` if needed, point `.vscode/settings.json` at the new `.venv`, and add a row to the index handover.
