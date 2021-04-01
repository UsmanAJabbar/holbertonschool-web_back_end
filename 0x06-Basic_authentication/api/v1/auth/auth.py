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
        """
        if not request:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        --------------------
        METHOD: current_user
        --------------------
        """
        return None
