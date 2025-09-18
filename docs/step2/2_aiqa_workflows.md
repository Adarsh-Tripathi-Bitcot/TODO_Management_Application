# AIQA Workflows

## Overview
This document records how automated quality assurance and intelligent workflows are being set up to maintain high development standards.

## What I Have Done
- Established automated quality checks using:
  - **Black** for code formatting.
  - **Ruff** for linting.
  - **Pytest** for testing with coverage reporting.
- Configured the project to run these tools locally before commits via pre-commit hooks.

## What I Am Doing
- Designing fixtures and test database setup to enable realistic async testing of FastAPI endpoints.

## What I Will Do
- Add test coverage thresholds and badges (via Codecov or coverage.py HTML reports).
- Expand test cases as the API grows to ensure we hit >95% coverage consistently.



