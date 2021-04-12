#!/usr/bin/env python3
"""Hash Password File"""
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """
    ----------------------
    METHOD: _hash_password
    ----------------------
    Description:
        Returns a hashed password from a
        plain text password passed in the
        variable @password
    """
    if type(password) is str:
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
    return str(uuid.uuid4())


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

    def get_user_from_session_id(self, session_id: str):
        """
        --------------------------------
        METHOD: get_user_from_session_id
        --------------------------------
        Description:
            Takes in a session ID and returns
            the user, otherwise none
        """
        if session_id and type(session_id) is str:
            try:
                return self._db.find_user_by(session_id=session_id)
            except NoResultFound:
                pass

    def destroy_session(self, user_id: int) -> None:
        """
        -----------------------
        METHOD: destroy_session
        -----------------------
        Description:
            Destroys a user session based from a given
            user_id.
        """
        if user_id:
            try:
                user = self._db.find_user_by(id=user_id)
                self._db.update_user(user.id, session_id=None)
            except NoResultFound:
                pass

    def get_reset_password_token(self, email: str) -> str:
        """
        --------------------------------
        METHOD: get_reset_password_token
        --------------------------------
        Description:
            Returns a password reset token
        """
        if type(email) is str:
            try:
                user = self._db.find_user_by(email=email)
                reset_token = _generate_uuid()
                self._db.update_user(user.id, reset_token=reset_token)
                return reset_token
            except NoResultFound:
                raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        -----------------------
        METHOD: update_password
        -----------------------
        Description:
            Updates the password in the database
        """
        if type(reset_token) is str and type(password) is str:
            try:
                user = self._db.find_user_by(reset_token=reset_token)
                self._db.update_user(user.id,
                                     hashed_password=_hash_password(password),
                                     reset_token=None)
            except NoResultFound:
                raise ValueError
