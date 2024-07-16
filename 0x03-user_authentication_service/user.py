#!/usr/bin/env python3
"""
    Module implementing a SQLAlchemy User model

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """class User that inherits from the Base class"""

    __table__ = "users"

    id = Column(Integer, primary_key=True, auto_increment=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
