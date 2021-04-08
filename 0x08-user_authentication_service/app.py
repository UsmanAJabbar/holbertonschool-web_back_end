#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    -------------
    METHOD: login
    -------------
    Description:
        Takes in a username and password from a post
        request to the API and returns whether the
        login with the given details was successful.
    """
    post_data = dict(request.form)

    if post_data and 'email' in post_data and 'password' in post_data:
        if AUTH.valid_login(post_data['email'], post_data['password']):

            session_id = AUTH.create_session(post_data['email'])
            login = jsonify({"email": post_data['email'],
                             "message": "logged in"})
            login.set_cookie('session_id', session_id)
            return login, 200

    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    --------------
    METHOD: logout
    --------------
    Description:
        Takes in a username and password
        and deletes a session
    """
    post_data = dict(request.form)

    if post_data and 'email' in post_data and 'password' in post_data:
        if AUTH.valid_login(post_data['email'], post_data['password']):
            session_id = request.cookies.get('session_id')
            if session_id:
                user = AUTH.get_user_from_session_id(session_id)
                if user:
                    AUTH.destroy_session(user.user_id)
                    return redirect('/')
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")