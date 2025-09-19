# src/schemas/user.py
from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    """
    Pydantic schema for user registration data.
    
    Attributes:
        email (EmailStr): The user's email address.
        password (str): The user's password.
    """
    email: EmailStr
    password: str
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """
        Validate the user's password to ensure it meets security requirements.
        
        Args:
            v (str): The password to validate.

        Returns:
            str: The validated password.

        Raises:
            ValueError: If the password does not meet security requirements.
        """
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number')
        if not re.search(r'\d', v):
            raise ValueError('Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number')
        return v

class UserLogin(BaseModel):
    """
    Pydantic schema for user login data.
    
    Attributes:
        email (EmailStr): The user's email address.
        password (str): The user's password.
    """
    email: EmailStr
    password: str

class UserOut(BaseModel):
    """
    Pydantic schema for user data returned after registration.
    
    Attributes:
        id (int): The user's ID.
        email (EmailStr): The user's email address.
    """
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # Pydantic V2: tells Pydantic to treat the SQLAlchemy model as a dict
