# Project Setup

## Overview
This document records the setup activities for the TODO Management Application backend during Step 2 of the SDLC roadmap. The objective is to establish a robust foundation for development by creating a well-structured repository, configuring tooling, and preparing the environment for API and database implementation.

## What I Have Done
- Created a dedicated `feat/step2` branch from `develop`.
- Initialized the project folder `TODO_Management_Application` with clear SDLC-aligned structure.
- Added base configuration files:
  - `pyproject.toml` for dependency management and Black/Ruff settings.
  - `pytest.ini` and `setup.cfg` for testing and linting integration.
  - `requirements.txt` capturing initial dependencies (FastAPI, SQLAlchemy, Alembic, Pydantic, Pytest).
  - `.env` and `.env.example` for environment variables.
- Added `docs/` folder with Step-1 deliverables for traceability.
- Created `migrations/` folder and Alembic initialization (`env.py`, `script.py.mako`).

## What I Am Doing
- Verifying the project runs locally.
- Ensuring pre-commit hooks (Black, Ruff) are functional.

## What I Will Do
- Add CI workflows (GitHub Actions) to automatically run tests and linters on each PR.
- Extend the Alembic setup with a base migration including `users` and `todos` tables.
- Finalize environment-based configurations for dev/test/prod.

## Outcome
The repository now forms a solid backbone for Step 3 — API implementation and testing.
