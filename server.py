from flask import Flask, request
import json

app = Flask(__name__)

with open("db.json", "r") as f:
    data = json.load(f)

messages = data["messages"]

def write_message(message):
    messages.append(message)
    with open("db.json", "w") as f:
        json.dump(data, f)

    return "Message added"


@app.route("/messages", methods=["POST"])
def add_message():
    message = request.json
    return write_message(message)

@app.route("/messages", methods=["GET"])
def get_messages():
    return messages


if __name__ == "__main__":
    app.run()
