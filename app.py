import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # Use the API key directly in the URL
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyBwAqsDBa8dxrs9AqlHd73sADZ3okfc8cs"
    response = requests.post(url, json=request.json)
    return jsonify(response.json())

if __name__ == '__main__':
    # Render requires binding to 0.0.0.0 and the PORT environment variable
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
