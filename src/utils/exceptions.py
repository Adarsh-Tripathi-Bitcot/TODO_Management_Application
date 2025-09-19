# src/utils/exceptions.py
from fastapi import HTTPException, status

class TodoAppException(Exception):
    """Base exception for Todo App"""
    pass

class UserNotFoundError(TodoAppException):
    """Raised when user is not found"""
    pass

class TodoNotFoundError(TodoAppException):
    """Raised when todo is not found"""
    pass

class InvalidCredentialsError(TodoAppException):
    """Raised when credentials are invalid"""
    pass

class DuplicateEmailError(TodoAppException):
    """Raised when trying to create user with existing email"""
    pass
