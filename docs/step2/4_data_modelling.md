# Data Modelling

## Overview
This document outlines the data modeling activities for the TODO Management Application, including entity relationships and schema evolution strategy.

## What I Have Done
- Defined `User` and `Todo` entities with one-to-many relationship:
  - `users` table with id, email, password (hashed), created_at.
  - `todos` table with id, user_id, title, status, due_date, created_at, updated_at.
- Created initial ERD under `docs/assets` to visualize relationships.
- Initialized Alembic migrations to handle schema versions.

## What I Am Doing
- Implementing SQLAlchemy models reflecting the ERD.
- Configuring Alembic to autogenerate migrations and apply them to local/test DBs.

## What I Will Do
- Add indexes on `user_id`, `status`, and `due_date` to improve performance.
- Introduce SQLAlchemy mixins for timestamps and soft deletes if needed.
- Seed sample data for development/testing purposes.

![TODO App Data Model](../docs/assets/todo_app_data_model.png)

## Outcome
A normalized relational schema is in place, enabling secure, scalable data persistence and easy migration paths for future features.
