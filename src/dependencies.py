# src/dependencies.py
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from fastapi import Depends
from src.config import DATABASE_URL

# Database connection and session setup
engine = create_engine(DATABASE_URL)  # type: ignore
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Session:
    """
    Dependency to get the database session.
    
    Yields:
        Session: A SQLAlchemy session object to interact with the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
