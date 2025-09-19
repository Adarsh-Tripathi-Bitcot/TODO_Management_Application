# src/models/user.py
from sqlalchemy import Column, Integer, String, TIMESTAMP
# from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.dependencies import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # todos = relationship("Todo", back_populates="user")
