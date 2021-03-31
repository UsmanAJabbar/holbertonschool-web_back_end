#!/usr/bin/env python3
"""Basic Authentication Class File"""
from .auth import Auth
from typing import Tuple


class BasicAuth(Auth):
    """
    ----------------
    CLASS: BasicAuth
    ----------------
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str)\
            -> str:
        """
        -------------------------------------------
        METHOD: extract_base64_authorization_header
        -------------------------------------------
        """
        if not authorization_header or\
           type(authorization_header) is not str or\
           len(authorization_header) < 7 or\
           'Basic ' not in authorization_header:
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """
        ------------------------------------------
        METHOD: decode_base64_authorization_header
        ------------------------------------------
        """
        import base64
        import binascii

        if type(base64_authorization_header) is not str:
            return None

        try:
            return base64.b64decode(base64_authorization_header).decode()
        except binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str)\
                                 -> (str, str):
        """
        ------------------------------------------
        METHOD: decode_base64_authorization_header
        ------------------------------------------
        """
        if type(decoded_base64_authorization_header) is not str or\
           len(decoded_base64_authorization_header) <= 3 or\
           ':' not in decoded_base64_authorization_header:
            return (None, None)

        u_pass = decoded_base64_authorization_header.split(':')
        username, password = u_pass[0], u_pass[1]
        return (username, password)