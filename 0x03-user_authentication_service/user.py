#!/usr/bin/env python3
"""
    Module implementing a SQLAlchemy User model

"""
import logging
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

logging.basicConfig()
logging.getLogger('sqlalchemmy.engine').setLevel(logging.WARNING)


Base = declarative_base()


class User(Base):
    """class User that inherits from the Base class"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
