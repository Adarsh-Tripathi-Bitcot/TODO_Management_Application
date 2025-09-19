# src/services/auth.py
from sqlalchemy.orm import Session
from src.repositories.user import UserRepository
from src.utils.auth import hash_password, verify_password, create_jwt
from fastapi import HTTPException, status

def register_user(user_data, db: Session):
    """Handles user registration: hashes password and stores user in the DB."""
    user_repo = UserRepository(db)
    
    # Check if user already exists
    if user_repo.user_exists(user_data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = hash_password(user_data.password)
    db_user = user_repo.create_user(user_data.email, hashed_password)
    return db_user

def login_user(user_data, db: Session):
    """Handles user login: verifies password and generates JWT token."""
    user_repo = UserRepository(db)
    db_user = user_repo.get_by_email(user_data.email)
    
    if not db_user or not verify_password(user_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_jwt(db_user.id)
    return {"access_token": access_token, "token_type": "bearer"}
