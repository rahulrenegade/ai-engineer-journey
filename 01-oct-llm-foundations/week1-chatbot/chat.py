import ollama

MODEL = "llama3.2:3b"
SYSTEM_PROMPT = "You are a witty assistant who is helpful, creative, and friendly."
GREETINGS = "Assistant: Hello! How can I assist you today? "
last_input_tokens = 0
last_output_tokens = 0
print(GREETINGS)


def new_conversation():
    return [{"role": "system", "content": SYSTEM_PROMPT}]


messages = new_conversation()

while True:
    question = input("\nYou: ")
    if not question.strip():
        print("Please enter a question or command.")
        continue
    if question.lower() in ["/exit", "/quit"]:
        break
    elif question.lower() in ["/reset", "/clear"]:
        messages = new_conversation()
        last_input_tokens = 0
        last_output_tokens = 0
        print("Conversation reset.")
        print(GREETINGS)
        continue
    elif question.lower() in ["/tokens", "/token_count"]:
        print("input tokens : ", last_input_tokens)
        print("output tokens : ", last_output_tokens)
        continue

    messages.append({"role": "user", "content": question})
    response = ollama.chat(model=MODEL, messages=messages, stream=True)
    print("Assistant: ", end="", flush=True)
    reply = ""
    for chunk in response:
        reply += chunk.message.content
        print(chunk.message.content, end="", flush=True)
    messages.append(
        {
            "role": "assistant",
            "content": reply,
        }
    )
    last_input_tokens = chunk.prompt_eval_count
    last_output_tokens = chunk.eval_count
