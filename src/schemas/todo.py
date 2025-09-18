from pydantic import BaseModel
from datetime import date
from enum import Enum

class TodoStatus(Enum):
    todo = "todo"
    in_progress = "in progress"
    completed = "completed"

class TodoCreate(BaseModel):
    title: str
    due_date: date | None = None
    status: TodoStatus = TodoStatus.todo

class TodoUpdate(BaseModel):
    title: str | None = None
    due_date: date | None = None
    status: TodoStatus | None = None