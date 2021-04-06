#!/usr/bin/env python3
"""Authentication Class File"""


class Auth:
    """
    -----------
    CLASS: AUTH
    -----------
    """
    from flask import request
    from typing import TypeVar, List

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        --------------------
        METHOD: require_auth
        --------------------
        """
        if not path or not excluded_paths:
            return True

        def _asterisk(excluded_paths: list) -> list:
            """
            ---------------
            Returns a list of strings that end in '*'/
            ---------------
            """
            asterisked = []
            for path in excluded_paths:
                if path[-1] == '*':
                    asterisked.append(path[:-1])
            return asterisked

        ast = _asterisk(excluded_paths)
        if ast:
            if path[-1] == '/':
                path = path[-1]
            for path_wo_ast in ast:
                if path_wo_ast in path:
                    return False
            return True

        return path not in excluded_paths and\
            f'{path}/' not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """
        ----------------------------
        METHOD: authorization_header
        ----------------------------
        Description:
            Looks for a header called Authorization,
            and returns the value associated with it.
        """
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        --------------------
        METHOD: current_user
        --------------------
        """
        return None

    def session_cookie(self, request=None):
        """
        ----------------------
        METHOD: session_cookie
        ----------------------
        Description:
            Takes in a Flask request and returns
            the cookie value stored in the session ID.
        """
        if type(request) is not None:
            from os import environ as env

            session_name = env.get('SESSION_NAME')
            return request.cookies.get(session_name)