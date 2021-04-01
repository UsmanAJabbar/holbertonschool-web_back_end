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
        return not path or not excluded_paths or\
            path not in excluded_paths and\
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
