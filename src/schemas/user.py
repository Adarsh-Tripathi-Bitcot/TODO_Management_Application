from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @field_validator('password')
    def validate_password(cls, v):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', v):
            raise ValueError("Weak password")
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenData(BaseModel):
    email: str | None = None