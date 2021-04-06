#!/usr/bin/env python3
""" Session Auth Flask API """
from api.v1.views import app_views, User
from flask import request, jsonify


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    -------------
    METHOD: login
    -------------
    Description:
            Takes in login parameters
            and handles session logins
    """
    email, pwd = request.form.get('email'), request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    if not user[0].is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    from os import environ as env

    session_id = auth.create_session(user[0].id)
    session_name = env.get('SESSION_NAME')

    user_object = jsonify(user[0].to_json())
    user_object.set_cookie(session_name, session_id)

    return user_object


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """
    --------------
    METHOD: logout
    --------------
    Description:
            If a user's logged in, it logs them out,
            removing the session id from the system.
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
