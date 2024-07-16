#!/usr/bin/env python3
"""
    Module implementing a basic flask application

"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Defaulf app route with GET method that returns
    json payload"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
