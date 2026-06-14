import os
from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# The mobile-optimized interface
HTML_TERMINAL = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { background: black; color: #ffbf00; font-family: monospace; padding: 10px; margin: 0; }
        #logs { height: 80vh; overflow-y: scroll; border: 1px solid #333; margin-bottom: 10px; padding: 5px; font-size: 14px; }
        .control-area { display: flex; gap: 5px; }
        #in { flex-grow: 1; padding: 10px; background: #111; color: white; border: 1px solid #ffbf00; }
        button { padding: 10px; background: #ffbf00; color: black; border: none; font-weight: bold; }
    </style>
</head>
<body>
    <div id="logs">System: Conduit established.</div>
    <div class="control-area">
        <input id="in" placeholder="Enter command...">
        <button onclick="send()">Send</button>
    </div>
    <script>
        async function send() {
            let input = document.getElementById('in');
            let logs = document.getElementById('logs');
            let txt = input.value;
            if(!txt) return;
            logs.innerHTML += "<br>> James: " + txt;
            input.value = "";
            logs.scrollTop = logs.scrollHeight;
            
            let res = await fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({"contents": [{"parts": [{"text": txt}]}]})
            });
            let data = await res.json();
            let reply = data.candidates[0].content.parts[0].text;
            logs.innerHTML += "<br>> Gemini: " + reply;
            logs.scrollTop = logs.scrollHeight;
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
    # Ensure you replace YOUR_API_KEY with your actual key from AI Studio
    api_key = "AQ.Ab8RN6LIOrDGg3-eGeq5LWfGrEiNQLRDPxj-qOMmA6gwQ8-vpg"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    response = requests.post(url, json=request.json)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
  
