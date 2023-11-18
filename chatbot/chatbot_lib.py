import openai

api_key = "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"

client = openai.OpenAI(api_key=api_key)


def chat_with_gpt(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

    return completion.choices[0].message.content.strip()
