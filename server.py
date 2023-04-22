from flask import Flask
import json

app = Flask(__name__)

with open("db.json", "r") as f:
    data = json.load(f)

messages = data["messages"]


@app.route("/messages", methods=["POST"])
def write_message(message):
    messages.append(message)
    with open("db.json", "w") as f:
        json.dump(data, f)


@app.route("/messages", methods=["GET"])
def get_messages():
    return messages


if __name__ == "__main__":
    app.run()
