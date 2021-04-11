#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:

    def __init__(self):
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        ----------------
        METHOD: add_user
        ----------------
        Description:
            Adds a user to the database
        """
        if type(email) is str and type(hashed_password) in [str, bytes]:
            from user import User
            user = User(email=email, hashed_password=hashed_password)
            self._session.add(user)
            self._session.commit()
            return user

    def find_user_by(self, **kwargs: dict):
        """
        ---------------------
        METHODS: find_user_by
        ---------------------
        Description:
            Takes in an argument and looks for
            a row in the database that matches
            kwargs.
        """
        if not kwargs:
            raise InvalidRequestError

        for key in kwargs:
            if not hasattr(User, key):
                raise InvalidRequestError

        data = self._session.query(User).filter_by(**kwargs).one()
        return data

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """
        -------------------
        METHOD: update_user
        -------------------
        Description:
            Updates a given user with the attributes
            passed in kwargs.
        """
        if type(user_id) is int and type(kwargs) is dict:
            try:
                user = self.find_user_by(id=user_id)
                for key, value in kwargs.items():
                    if hasattr(User, key):
                        setattr(user, key, value)
                        self._session.commit()
                    else:
                        raise ValueError
            except NoResultFound:
                pass
