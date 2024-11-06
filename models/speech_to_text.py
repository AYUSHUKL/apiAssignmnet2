from google.cloud import speech

def convert_speech_to_text(audio):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio.read())
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US"
    )
    response = client.recognize(config=config, audio=audio)
    text = response.results[0].alternatives[0].transcript
    return text
