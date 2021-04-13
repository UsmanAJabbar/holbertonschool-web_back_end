#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.orm.exc import NoResultFound
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
    if post.keys() >= {'email', 'password'}:
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
    if post_data.keys() >= {'email', 'password'}:
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
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect('/')
    abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    ---------------
    METHOD: profile
    ---------------
    Description:
        Returns a the email of a user from
        a given session_id embedded in the
        cookies of the request
    """
    session_id = request.cookies.get('session_id')
    if session_id:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def reset_password():
    """
    ----------------------
    METHOD: reset_password
    ----------------------
    Description:
        Gets a user, generates and assigns the reset_tokken,
        and returns the reset token.
    """
    post_data = dict(request.form)
    if 'email' in post_data:
        try:
            user = AUTH._db.find_user_by(email=post_data['email'])
            reset_token = AUTH.get_reset_password_token(user.email)
            return jsonify({"email": user.email,
                            "reset_token": reset_token}), 200
        except ValueError:
            pass
    abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """
    -----------------------
    METHOD: update_password
    -----------------------
    Description:
        Updates the password from a
        put request to the /reset_password
        API.
    """
    pdata = dict(request.form)
    if pdata.keys() >= {'email', 'reset_token', 'new_password'}:
        try:
            AUTH.update_password(pdata['reset_token'], pdata['new_password'])
            return jsonify({"email": pdata['email'],
                            "message": "Password updated"}), 200
        except ValueError:
            pass
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
