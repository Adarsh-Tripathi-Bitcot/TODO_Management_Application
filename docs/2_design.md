# 2. Design & Technology Stack

## 2.1 Technology Stack Selection

| Component | Choice | Reason |
|-----------|--------|---------|
| **Backend** | FastAPI (Python 3.12+) | High performance async; OpenAPI auto-docs |
| **Database** | PostgreSQL | ACID, scalability, reliable transactions |
| **ORM** | SQLAlchemy 2.0 | Modern, typed queries, relationships |
| **Migrations** | Alembic | Version-controlled, zero-downtime migrations |
| **Auth** | JWT via PyJWT | Secure, standards-compliant tokenization |
| **Validation** | Pydantic v2 | Strong runtime validation, detailed errors |
| **Testing** | pytest + coverage | Async support, industry standard |

## 2.2 Layered Design
- **API Layer:** FastAPI routers handle HTTP.
- **Service Layer:** Business rules & validation.
- **Repository Layer:** SQLAlchemy sessions.
- **Auth Layer:** JWT + bcrypt.
- **Schema Layer:** Pydantic models (input/output).
- **Test Layer:** Fixtures, mocks, coverage.

## 2.3 Security Considerations
- Passwords hashed with bcrypt, salted.
- JWT expiration: 24h default.
- Refresh tokens can be added later.
- Rate limiting & CORS configurable.

## 2.4 Testing Strategy
- Unit tests per module.
- Integration tests with test DB.
- Coverage threshold ≥ 95%.