# src/routers/auth.py
from fastapi import APIRouter, Depends, status
from src.services.auth import register_user, login_user
from src.schemas.user import UserCreate, UserOut, UserLogin
from sqlalchemy.orm import Session
from src.dependencies import get_db

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)) -> UserOut:
    """
    Register a new user and return the user's ID and success message.
    
    Args:
        user (UserCreate): The user registration data.
        db (Session): The database session.

    Returns:
        UserOut: The registered user's data.
    """
    return register_user(user, db)

@router.post("/login", response_model=dict)
def login(user: UserLogin, db: Session = Depends(get_db)) -> dict:
    """
    Login a user and return a JWT token.
    
    Args:
        user (UserLogin): The user login credentials.
        db (Session): The database session.

    Returns:
        dict: A dictionary containing the access token and token type.
    """
    return login_user(user, db)
