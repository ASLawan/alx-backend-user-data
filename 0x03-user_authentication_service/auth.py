#!/usr/bin/env
"""
    Module implementing a function that hashes a password
    returns hashed password

"""
import bcrypt
import uuid
from db import DB
from typing import Optional
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes password using bcrypt, returns the hashed password"""
    salt = bcrypt.gensalt()
    hashedpwd = bcrypt.hashpw(password.encode("utf8"), salt)

    return hashedpwd


def _generate_uuid():
    """Generates a new uuid and returns it as a string"""
    return str(uuid.uuid4())


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

    def create_session(self, email: str) -> str:
        """Creates a session ID for a user and store in the database"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id:
                                 Optional[str]) -> Optional[User]:
        """Gets user from session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys current session for a given user based on user id"""
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            pass
