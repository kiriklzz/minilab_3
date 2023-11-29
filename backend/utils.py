# utils.py
from flask import jsonify, send_file, send_from_directory
from PIL import Image
from io import BytesIO
import os
import requests
from config import Config
def get_random_photo():
    unsplash_api_url = 'https://api.unsplash.com/photos/random'
    headers = {'Authorization': f'Client-ID {Config.UNSPLASH_ACCESS_KEY}'}

    response = requests.get(unsplash_api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        photo_url = data['urls']['regular']

        image_data = requests.get(photo_url).content
        image = Image.open(BytesIO(image_data))

        img_io = BytesIO()
        image.save(img_io, 'JPEG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/jpeg')
    else:
        return jsonify({'error': 'Failed to fetch random photo from Unsplash'}), 500


def upload_photo(request):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    image = Image.open(file)
    resized_image = image.resize((300, 300))

    output_buffer = BytesIO()
    resized_image.save(output_buffer, format="JPEG")

    return send_file(BytesIO(output_buffer.getvalue()), mimetype='image/jpeg')


def get_frontend_path(filename):
    return send_from_directory(os.path.join(os.path.dirname(__file__), '..', 'frontend'), filename)
