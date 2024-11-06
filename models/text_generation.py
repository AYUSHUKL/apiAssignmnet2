import openai

def generate_text(input_text):
    openai.api_key = 'api'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": input_text}
        ],
        max_tokens=400
    )
    return response.choices[0].message['content'].strip()
