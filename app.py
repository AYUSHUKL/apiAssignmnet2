import pyttsx3
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from models.text_generation import generate_text
from models.sentiment_analysis import analyze_sentiment
from models.ner import extract_entities
from models.text_summarization import summarize_text
from models.speech_to_text import convert_speech_to_text
from models.create_image import generate_image  # Make sure to add this file
import PyPDF2  # Import PyPDF2
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:8000"}})  # Allow requests from your frontend origin

# Ensure the static directory exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/generate_text', methods=['POST'])
def generate_text_endpoint():
    data = request.json
    input_text = data['input_text']
    result = generate_text(input_text)
    return jsonify({'generated_text': result})

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_endpoint():
    data = request.json
    input_text = data['input_text']
    result = analyze_sentiment(input_text)
    return jsonify({'sentiment': result})

@app.route('/extract_entities', methods=['POST'])
def extract_entities_endpoint():
    data = request.json
    input_text = data['input_text']
    result = extract_entities(input_text)
    return jsonify({'entities': result})

@app.route('/summarize_text', methods=['POST'])
def summarize_text_endpoint():
    data = request.json
    input_text = data['input_text']
    result = summarize_text(input_text)
    return jsonify({'summary': result})

@app.route('/convert_speech_to_text', methods=['POST'])
def convert_speech_to_text_endpoint():
    audio = request.files['audio']
    result = convert_speech_to_text(audio)
    return jsonify({'text': result})

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    result = summarize_text(text)
    return jsonify({'summary': result})

@app.route('/generate_image', methods=['POST'])
def generate_image_endpoint():
    data = request.json
    prompt = data['prompt']
    result = generate_image(prompt)
    return jsonify({'image': result})

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech_endpoint():
    data = request.json
    input_text = data['input_text']
    engine = pyttsx3.init()
    output_path = os.path.join('static', 'output.mp3')
    engine.save_to_file(input_text, output_path)
    engine.runAndWait()
    return jsonify({'audio_file': 'output.mp3'})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
