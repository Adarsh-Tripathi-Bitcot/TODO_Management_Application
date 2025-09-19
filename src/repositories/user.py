# src/repositories/user.py

from sqlalchemy.orm import Session
from src.models.user import User
from src.repositories.base import BaseRepository
from typing import Optional

class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email address."""
        return self.db.query(self.model).filter(self.model.email == email).first()

    def create_user(self, email: str, password: str) -> User:
        """Create a new user with email and hashed password."""
        user_data = {
            "email": email,
            "password": password
        }
        return self.create(user_data)

    def user_exists(self, email: str) -> bool:
        """Check if user with email already exists."""
        return self.get_by_email(email) is not None
