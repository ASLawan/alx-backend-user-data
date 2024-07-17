#!/usr/bin/env python3
"""
    Module implementing a DB class

"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initializes a new DB instance"""
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a new user to the database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Finds a user based given kwargs"""
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            return user
        except Exception:
            raise InvalidRequestError
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates user attributes if user is found"""
        try:
            user = self.find_user_by(id=user_id)
        except Exception:
            raise NoResultFound

        for k, v in kwargs.items():
            if not hasattr(user, k):
                raise ValueError
            setattr(user, k, v)
        self._session.add(user)
        self._session.commit()
