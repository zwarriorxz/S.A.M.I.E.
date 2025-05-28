from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/submit', methods=['POST'])  # ✅ only the route path
def receive_text():
    data = request.json
    text = data.get('text', '')
    print(f"Received text: {text}")
    return jsonify({'response': f'Server received: {text}'})

if __name__ == '__main__':
    app.run(debug=True)
