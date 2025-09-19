# src/utils/auth.py
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from src.config import JWT_SECRET_KEY

# Initialize password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60  # 24 hours

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against the stored hash.
    
    Args:
        plain_password (str): The plain text password to verify.
        hashed_password (str): The hashed password to compare with.

    Returns:
        bool: True if the password is correct, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_jwt(user_id: int) -> str:
    """
    Generate a JWT token with a 24-hour expiration.
    
    Args:
        user_id (int): The ID of the user.

    Returns:
        str: The JWT token.
    """
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(user_id)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def verify_jwt(token: str) -> dict:
    """
    Verify a JWT token and return the payload.
    
    Args:
        token (str): The JWT token to verify.

    Returns:
        dict: The decoded payload.
    
    Raises:
        HTTPException: If the token is invalid.
    """
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise JWTError("Invalid token")
        return {"id": int(user_id)}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Get current user from JWT token.
    
    Args:
        token (str): The JWT token to extract user information from.

    Returns:
        dict: The user's data extracted from the token.
    """
    return verify_jwt(token)
