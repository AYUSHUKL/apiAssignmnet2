import openai

def generate_text(input_text):
    openai.api_key = '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'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ],
        max_tokens=400
    )
    return response.choices[0].message['content'].strip()
