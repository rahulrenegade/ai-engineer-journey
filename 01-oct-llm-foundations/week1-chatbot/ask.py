import ollama

question = input("What can i help you with today? ")

response = ollama.chat(
    model="llama3.2:3b",
    messages=[  # the model's earlier reply
        {"role": "user", "content": question},  # the new question
    ],
)

print(response.message.content)
print("------------------------------------")
print("input tokens :", response.prompt_eval_count)
print("output tokens :", response.eval_count)
print("seconds taken :", response.total_duration / 1e9)
