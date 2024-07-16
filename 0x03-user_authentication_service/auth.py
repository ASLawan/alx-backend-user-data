#!/usr/bin/env
"""
    Module implementing a function that hashes a password
    returns hashed password

"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes password using bcrypt, returns the hashed password"""
    salt = bcrypt.gensalt()
    hashedpwd = bcrypt.hashpw(password.encode("utf8"), salt)

    return hashedpwd


class Auth:
    """Auth class to interact with the authentication database"""

    def __init__(self):
        """initializes DB instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers user with given attributes"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashedpwd = _hash_password(password)
            new_user = self._db.add_user(email=email,
                                         hashed_password=hashedpwd)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if password is valid by comparing the two hashes"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        if bcrypt.checkpw(password.encode(), user.hashed_password):
            return True
        return False
