from flask import Flask, jsonify

app = Flask(__name__)

count = 0
@app.route("/")
def hello_world():
    global count
    count += 1
    return jsonify(
        text="Hello, flask",
        count=count
    )