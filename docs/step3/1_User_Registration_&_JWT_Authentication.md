# Step 3.1: User Registration & JWT Authentication

## Overview
This step covers the implementation of the user registration and login functionalities, utilizing **FastAPI**, **Pydantic** for validation, **bcrypt** for password hashing, and **JWT** for authentication. We will also add necessary migrations, configurations, and testing.

## Steps

### 1. **Set Up Authentication Router**
We created the `auth.py` file in the `routers/` folder to define the routes for user registration (`/register`) and login (`/login`).

### 2. **Implement Authentication Logic**
- Implemented `register_user` to handle user registration and password hashing.
- Implemented `login_user` to verify credentials and generate a JWT token.

### 3. **Hash Password and Generate JWT**
- Created utility functions in `auth.py` to hash passwords with bcrypt and generate JWT tokens using **PyJWT**.

### 4. **Create SQLAlchemy User Model**
- Defined the `User` model to store user data, including the email and hashed password.

### 5. **Create Pydantic Models**
- Created `UserCreate` and `UserLogin` models for request validation.

### 6. **Add Database Dependency Injection**
- Created `get_db` to handle session management for database interactions.

### 7. **Create Migration for User Table**
- Used Alembic to create the necessary migration for the `users` table.

### 8. **Write Tests**
- Created test cases for both the registration and login routes using **pytest**.

## User Registration & Login Endpoints

```json
1. User Registration Endpoint

Endpoint: `/auth/register`
Method: `POST`

Request Body Example:
{
  "email": "testuser@example.com",
  "password": "Test1234"
}

Response (201 Created):
{
  "id": 1,
  "email": "testuser@example.com"
}
Explanation:
After a successful registration, the server responds with the newly created user’s id and email.

The password is hashed and stored securely in the database, and a user record is created.

Error Handling:
If the email is already in use, the system will return a 400 Bad Request with the error message:

{ "detail": "Email already registered" }
If the password does not meet the security requirements (e.g., less than 8 characters, missing digits, etc.), the system will return a 422 Unprocessable Entity error:

{ "detail": "Password must be at least 8 characters long and contain at least one number and one letter" }


2. User Login Endpoint
Endpoint: /auth/login
Method: POST

Request Body Example:
{
  "email": "testuser@example.com",
  "password": "Test1234"
}

Response (200 OK):
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
JWT Token:
The token is returned in the access_token field. This token is used for authentication on subsequent requests, with the Authorization header set as Bearer <JWT_TOKEN>.

Explanation:
If the email and password match, a JWT token is generated and returned. The token contains the user’s ID and expiry information. This token is then used to authenticate requests to protected endpoints.

Error Handling:
If the email is not found or the password is incorrect, the system will return a 401 Unauthorized error:

{ "detail": "Invalid credentials" }
If required fields are missing (e.g., email or password), a 422 Unprocessable Entity error is returned:

{ "detail": "Email and password are required" }
```

## Setting Up Database for PostgreSQL

1. **Install PostgreSQL**:
    - Install PostgreSQL on your local machine.
    - Create a database named `todo_app_db`.

2. **Create a New Database**:
    ```sql
    CREATE DATABASE todo_app_db;
    ```

3. **Generate a JWT Secret Key**:
    ```
    import secrets
        # Generate a 256-bit secret key (32 bytes) in hexadecimal format
    jwt_secret = secrets.token_hex(32)
    print(jwt_secret)

    ```

4. **Configure .env File**:
    Update `.env` with:
    ```env
    DATABASE_URL=postgresql://username:password@localhost/db_name
    JWT_SECRET_KEY=<your_generated_key>
    ```

### Verifying Implementation

1. **Start FastAPI Server**:
    ```bash
    uvicorn src.main:app --reload
    ```

2. **Run Tests**:
    ```bash
    pytest tests/test_auth.py
    ```

This will ensure everything works as expected.
