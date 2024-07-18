#!/usr/bin/env python3
"""
    Module implementing a basic flask application

"""
from flask import (Flask, jsonify, request, abort,
                   make_response, redirect, url_for)
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    """Defaulf app route with GET method that returns
    json payload"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
