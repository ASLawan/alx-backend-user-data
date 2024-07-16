#!/usr/bin/env
"""
    Module implementing a function that hashes a password
    returns hashed password

"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes password using bcrypt, returns the hashed password"""
    salt = bcrypt.gensalt()
    hashedpwd = bcrypt.hashpw(password.encode("utf8"), salt)

    return hashedpwd
