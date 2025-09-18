from sqlalchemy import Column, Integer, String, DATE, TIMESTAMP, Enum, ForeignKey, func
from app.models.base import Base
from sqlalchemy.orm import relationship
from enum import Enum as PythonEnum

class TodoStatus(PythonEnum):
    todo = "todo"
    in_progress = "in progress"
    completed = "completed"

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    status = Column(Enum(TodoStatus), nullable=False)
    due_date = Column(DATE, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="todos")