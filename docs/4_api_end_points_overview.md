# 4. API Endpoints Overview

## 4.1 REST Endpoints

| Endpoint | Method | Auth | Description |
|-----------|--------|------|-------------|
| /register | POST | No | Register new user |
| /login | POST | No | Login, get JWT token |
| /todos | GET | Yes | List user’s TODOs |
| /todos | POST | Yes | Create new TODO |
| /todos/{todo_id} | GET | Yes | Retrieve TODO by ID |
| /todos/{todo_id} | PUT | Yes | Update TODO by ID |
| /todos/{todo_id} | DELETE | Yes | Delete TODO by ID |

---

### 4.2 Sample Request/Responses

```json
Register (POST /register)

Request:
{ "email": "user@email.com", "password": "Password123" }

Response (201):
json
{ "id": 1, "message": "User registered successfully" }

Errors:
400 Invalid email/password
422 Missing fields


Login (POST /login)

Request:
json
{ "email": "user@email.com", "password": "Password123" }

Response (200):
json
{ "access_token": "<JWT>", "token_type": "bearer" }
Error (401):
json
{ "error": "Invalid credentials" }


Create TODO (POST /todos)

Request:
json
{ "title": "Sample Task", "due_date": "2025-09-25", "status": "todo" }

Response (201):
json
{ "id": 101, "message": "TODO created successfully" }

Error:
json
{ "error": "Status must be one of: todo, in progress, completed" }


List TODOs (GET /todos)

Response (200):
json
[ { "id": 101, "title": "Sample Task", "due_date": "2025-09-25", "status": "todo" } ]


```

### 4.3 Error Handling Standards

Invalid input → 400
Validation error → 422
Auth error → 401 or 403
Resource not found → 404
Conflict → 409

Consistent JSON error:
```json
{ "error": "Detailed message" }