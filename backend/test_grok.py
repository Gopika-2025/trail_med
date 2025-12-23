from groq import Groq

client = Groq(api_key="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")

completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Say hello in one sentence"}
    ],
    temperature=0.3
)

print(completion.choices[0].message.content)
