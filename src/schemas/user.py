# src/schemas/user.py
from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
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
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # Pydantic V2: tells Pydantic to treat the SQLAlchemy model as a dict
