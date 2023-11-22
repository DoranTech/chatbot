import openai

client = openai.OpenAI()


def chat_with_gpt(prompt):
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])

    return completion.choices[0].message.content.strip()
