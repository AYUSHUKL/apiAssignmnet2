import openai

def generate_image(prompt):
    openai.api_key = 'YOUR_OPENAI_API_KEY'
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']