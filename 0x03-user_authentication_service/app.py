#!/usr/bin/env python3
"""
    Module implementing a basic flask application

"""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def index():
    """Defaulf app route with GET method that returns
    json payload"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """Registers a new user if not exists already"""
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
