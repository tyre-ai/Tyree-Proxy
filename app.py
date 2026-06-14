HTML_TERMINAL = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: black; color: #ffbf00; font-family: monospace; padding: 20px; }
        #logs { height: 70vh; overflow-y: scroll; border: 1px solid #333; margin-bottom: 10px; }
        #in { width: 70%; padding: 10px; background: #111; color: white; border: 1px solid #ffbf00; }
        button { padding: 10px; background: #ffbf00; color: black; border: none; }
    </style>
</head>
<body>
    <div id="logs">System: Conduit established.</div>
    <input id="in" placeholder="Enter command..."><button onclick="send()">Send</button>
    <script>
        async function send() {
            let input = document.getElementById('in');
            let logs = document.getElementById('logs');
            let txt = input.value;
            logs.innerHTML += "<br>> James: " + txt;
            input.value = "";
            let res = await fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({"contents": [{"parts": [{"text": txt}]}]})
            });
            let data = await res.json();
            logs.innerHTML += "<br>> Gemini: " + data.candidates[0].content.parts[0].text;
        }
    </script>
</body>
</html>
""
