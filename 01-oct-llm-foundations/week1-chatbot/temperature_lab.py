import ollama

MODEL = "llama3.2:3b"

TEMPERATURES = [0, 0.7, 1.5]

RUNS = 3

PROMPT = "Invent a name for a new coffee shop. Reply with only the name."
messages = [{"role": "user", "content": PROMPT}]

for t in TEMPERATURES:
    print(f"\n\nTemperature: {t}")
    replies = []

    for _ in range(RUNS):
        response = ollama.chat(
            model=MODEL,
            messages=messages,
            options={"temperature": t},
        )
        replies.append(response.message.content)
    print(" / ".join(replies))
