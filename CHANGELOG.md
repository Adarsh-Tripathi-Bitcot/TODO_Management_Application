# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Changed
- **Step-2 Implementation:**  
  - Created `feat/step2` branch with full project setup under `TODO_Management_Application/`.
  - Added `docs/step2` covering project setup, AIQA workflows, project structure, and data modelling.
  - Established `src/` folder with layered architecture directories (`routers`, `services`, `repositories`, `models`, `schemas`, `utils`).
  - Initialized Alembic migrations with `env.py` and `script.py.mako`.
  - Added test scaffolding under `tests/`.

### Notes
- The repository now forms a solid backbone for Step-3 — API implementation and testing.


### Added
- **Project Planning Document** outlining architecture, scope, features, technology stack, and system design for the TODO Management Application.
- **Project skeleton and configuration files:**
  - `.gitignore` – placeholder for ignoring environment-specific files.
  - `.env` and `.env.example` – environment variable templates.
  - `.pre-commit-config.yaml` – base for code-quality and linting hooks.
  - `pyproject.toml` – initial project metadata and tool configuration.
  - `pytest.ini` – base testing configuration.
  - `setup.cfg` – configuration for style/lint/test tooling.

### Notes
- This is the initial setup phase laying down the foundation for scalable development.
- No application code has been implemented yet — the focus is on structure and consistency.
