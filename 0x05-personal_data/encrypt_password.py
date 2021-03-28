#!/usr/bin/env python3


def hash_password(password: str) -> bytes:
    """
    ---------------------
    METHOD: hash_password
    ---------------------
    Description:
        Takes in a string password and returns a
        hashed version of it
    Args:
        @password: password string
    """
    from bcrypt import hashpw, gensalt

    password, salt = bytes(password.encode('UTF-8')), bytes(gensalt())
    return hashpw(password, salt)
