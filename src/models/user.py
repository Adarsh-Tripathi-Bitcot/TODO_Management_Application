# src/models/user.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from src.dependencies import Base

class User(Base):
    """
    User model for the 'users' table in the database.
    
    Attributes:
        id (int): The user's ID (primary key).
        email (str): The user's email (unique and indexed).
        password (str): The user's hashed password.
        created_at (TIMESTAMP): The timestamp of when the user was created.
    """
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True)
    email: str = Column(String, unique=True, index=True)
    password: str = Column(String)
    created_at: TIMESTAMP = Column(TIMESTAMP, server_default=func.now())
