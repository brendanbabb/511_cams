from flask import Flask, request, send_file, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get('API_KEY')  # Store your API key as an environment variable

def fetch_webcam_image(camera_id):
    # Replace with the actual API endpoint
    api_url = f"https://api.example.com/webcams/{camera_id}/image"

    headers = {
        'Authorization': f'Bearer {API_KEY}',
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        image_path = f'{camera_id}.jpg'
        with open(image_path, 'wb') as f:
            f.write(response.content)
        return image_path
    else:
        return None

@app.route('/get_webcam_image', methods=['GET'])
def get_webcam_image():
    camera_id = request.args.get('camera_id')
    if not camera_id:
        return jsonify({'error': 'camera_id parameter is required'}), 400

    image_path = fetch_webcam_image(camera_id)
    if image_path:
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return jsonify({'error': 'Failed to fetch image'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
