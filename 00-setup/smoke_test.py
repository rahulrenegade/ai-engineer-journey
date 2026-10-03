"""Checks that your local model (Ollama) and cloud model (Gemini) both answer.

Run from inside 01-oct-llm-foundations/:
    uv run ../00-setup/smoke_test.py
"""

import os

from dotenv import find_dotenv, load_dotenv

# usecwd=True: look for .env in the folder you run from, not the script's folder
load_dotenv(find_dotenv(usecwd=True))

PROMPT = "In one sentence, what is a token in an LLM?"


def test_ollama():
    import ollama

    model = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    resp = ollama.chat(model=model, messages=[{"role": "user", "content": PROMPT}])
    print(f"[OK] Ollama ({model}): {resp['message']['content'].strip()}\n")


def test_gemini():
    from google import genai
    from google.genai import types

    key = os.getenv("GEMINI_API_KEY")
    if not key:
        print("[SKIP] Gemini: GEMINI_API_KEY not found in .env\n")
        return
    model = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
    client = genai.Client(api_key=key)
    # AFC off: in week 3 you'll write the tool-calling loop yourself
    config = types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
    )
    resp = client.models.generate_content(model=model, contents=PROMPT, config=config)
    print(f"[OK] Gemini ({model}): {resp.text.strip()}\n")


if __name__ == "__main__":
    for test in (test_ollama, test_gemini):
        try:
            test()
        except Exception as e:
            print(f"[FAIL] {test.__name__}: {e}\n")
