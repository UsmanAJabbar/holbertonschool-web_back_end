#!/usr/bin/env python3
"""Hash Password File"""
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    ----------------------
    METHOD: _hash_password
    ----------------------
    Description:
        Returns a hashed password from a
        plain text password passed in the
        variable @password
    """
    import bcrypt

    pwd, salt = password.encode(), bcrypt.gensalt()
    return bcrypt.hashpw(pwd, salt)


def _generate_uuid() -> str:
    """
    ----------------------
    METHOD: _generate_uuid
    ----------------------
    Description:
        Generates and returns a UUID
    """
    from uuid import uuid4
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database """


    def __init__(self):
        self._db = DB()


    def register_user(self, email: str, password: str) -> User:
        """
        ---------------------
        METHOD: register_user
        ---------------------
        Description:
            Registers and returns a new User while
            simuntaneously updating the database
            upon successful creation.
        """
        if type(email) is str and type(password) is str:

            try:
                self._db.find_user_by(email=email)
                raise ValueError(f'User {email} already exists')
            except NoResultFound:
                user = self._db.add_user(email, _hash_password(password))
                return user
    

    def valid_login(self, email: str, password: str) -> bool:
        """
        -------------------
        METHOD: valid_login
        -------------------
        Description:
            Returns whether a given password is valid
            for a given user.
        """
        import bcrypt

        if type(email) is str and type(password) is str:
            try:
                user = self._db.find_user_by(email=email)
                return bcrypt.checkpw(password.encode(), user.hashed_password)
            except NoResultFound:
                return False
        return False
    
    def create_session(self, email: str) -> str:
        """
        ----------------------
        METHOD: create_session
        ----------------------
        Description:
            Creates and returns a new session ID
        """
        if type(email) is str:
            try:
                user = self._db.find_user_by(email=email)
                session_id = _generate_uuid()
                setattr(user, 'session_id', session_id)
                return session_id
            except NoResultFound:
                return None