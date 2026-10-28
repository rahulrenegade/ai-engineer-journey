import ollama

MODEL = "llama3.2:3b"
SYSTEM_PROMPT = "You are a witty assistant who is helpful, creative, and friendly."

messages = [{"role": "system", "content": SYSTEM_PROMPT}]

TEMPERATURE = [0, 0.7, 1.5]

PROMPT = "Invent a name for a new coffee shop. Reply with only the name."
messages.append({"role": "user", "content": PROMPT})
for t in TEMPERATURE:
    print(f"\n\nTemperature: {t}")
    print("Assistant: ", end="", flush=True)
    for i in range(3):
        response = ollama.chat(
            model=MODEL,
            messages=messages,
            options={"temperature": t},
        )
        print(response.message.content, end=" | ", flush=True)
