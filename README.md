python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt


python app.py

python -m http.server 8000
