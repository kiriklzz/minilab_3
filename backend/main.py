# main.py
from flask import Flask, request
from utils import get_random_photo, upload_photo, get_frontend_path

app = Flask(__name__)


@app.route('/random_photo', methods=['GET'])
def random_photo():
    return get_random_photo()


@app.route('/upload_photo', methods=['POST'])
def upload():
    return upload_photo(request)


@app.route('/', methods=['GET'])
def upload_page():
    return get_frontend_path('index.html')


if __name__ == '__main__':
    app.run(debug=True)
