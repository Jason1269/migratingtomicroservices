from flask import flask

import os

app = FLASK(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/ping")
def pint():
    return "pong"

@app.route("/health")
def health():
    return "ok"

if __name__ == "__main__"
port = int(os.environ.get("PORT", 5000))
app.run(debug=TRUE, host='0.0.0.0', port = port)