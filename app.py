from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home(date: str):  # Format: "YYYY-MM-DD"
    pass


if __name__ == "__main__":
    port = 8080
    app.run(port=port)
