from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Planegy Postbot ist online."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
