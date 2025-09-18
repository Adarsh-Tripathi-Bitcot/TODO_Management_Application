from fastapi import HTTPException

# Custom exceptions for error handling
class AuthError(HTTPException):
    pass