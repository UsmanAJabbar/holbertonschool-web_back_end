#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def status():
    """
    --------------
    METHOD: status
    --------------
    Description:
        Returns the status of the flask API
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    -------------
    METHOD: users
    -------------
    Description:
        Takes in a username and a password and registers
        the user if the user with that email does not
        exist.
    """
    post = dict(request.form)
    if post and 'email' in post and 'password' in post:
        try:
            user = AUTH.register_user(post['email'], post['password'])
            return jsonify({"email": post['email'],
                            "message": "user created"}), 200
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")