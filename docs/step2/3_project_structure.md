# Step 2 – Project Structure

## Overview
This document captures the logical and physical structure of the TODO Management Application backend.

## What I Have Done
- Designed and implemented a clean, layered architecture under `src/`:

```
todo-management-application/
├── src/                  # Core application code
│   ├── __init__.py
│   ├── main.py           # Entry point: FastAPI app creation, middleware
│   ├── config.py         # Load .env, configs (e.g., DATABASE_URL)
│   ├── dependencies.py   # Dependency injection (e.g., get_current_user)
│   ├── routers/          # API layer: FastAPI routers
│   │   ├── __init__.py
│   │   ├── auth.py       # /register, /login endpoints
│   │   └── todos.py      # /todos endpoints
│   ├── services/         # Business logic layer: AuthService, TodoService
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── todos.py
│   ├── repositories/     # Persistence layer: AbstractRepo + SQLAlchemy impl
│   │   ├── __init__.py
│   │   ├── base.py       # Abstract base repository
│   │   ├── user.py       # UserRepository
│   │   └── todo.py       # TodoRepository
│   ├── models/           # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── todo.py
│   ├── schemas/          # Pydantic models for validation/serialization
│   │   ├── __init__.py
│   │   ├── user.py       # UserCreate, UserLogin, etc.
│   │   └── todo.py       # TodoCreate, TodoUpdate, etc.
│   └── utils/            # Helpers: JWT utils, password hashing, errors
│       ├── __init__.py
│       ├── auth.py       # create_jwt, verify_password
│       └── exceptions.py # Custom exceptions
├── tests/                # Test layer: pytest fixtures and tests
│   ├── __init__.py
│   ├── conftest.py       # Fixtures (e.g., test_db, client)
│   ├── test_auth.py
│   └── test_todos.py
├── migrations/           # Alembic migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions/         # Auto-generated migration files
├── .env.example          # Template for .env
├── README.md             # Expanded docs: setup, run, API usage
├── dev_requirements.txt
├── .env
├── .gitignore
├── CHANGELOG.md
├── setup.cfg
├── pytest.ini
├── pyproject.tomlz
├── .pre-commit-config.yaml
```


- Added `tests/` mirroring the main structure for easy maintainability.
- Prepared `migrations/` for Alembic to manage schema evolution.

## What I Am Doing
- Refining module boundaries (service vs repository vs router) to follow SOLID principles.
- Implementing placeholder files and docstrings in each module for consistency.

## What I Will Do
- Populate `models/` with SQLAlchemy models for `User` and `Todo` using Alembic migrations.
- Implement `schemas/` Pydantic models aligned with API specs.
- Connect routers, services, and repositories with dependency injection for clean testability.

## Outcome
The project structure reflects enterprise-grade design principles, making the codebase scalable, testable, and easy to maintain.