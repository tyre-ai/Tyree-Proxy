import os
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# This is your actual terminal interface
HTML_TERMINAL = """
<!DOCTYPE html>
<html>
<body style="background:black; color:amber; font-family:monospace;">
    <div id="logs">System: Conduit active.</div>
    <input id="in" style="background:black; color:white; width:90%;"><button onclick="send()">Send</button>
    <script>
        async function send() {
            let txt = document.getElementById('in').value;
            document.getElementById('logs').innerHTML += "<br>James: " + txt;
            let res = await fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({"contents": [{"parts": [{"text": txt}]}]})
            });
            let data = await res.json();
            document.getElementById('logs').innerHTML += "<br>Gemini: " + data.candidates[0].content.parts[0].text;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TERMINAL)

@app.route('/chat', methods=['POST'])
def chat():
    # Your existing AI logic here
    import requests
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=YOUR_API_KEY"
    response = requests.post(url, json=request.json)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
