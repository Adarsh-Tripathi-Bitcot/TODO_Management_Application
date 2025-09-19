# tests/test_auth.py
from fastapi.testclient import TestClient
from src.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import pytest
from src.dependencies import get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables
Base.metadata.create_all(bind=engine)

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def setup_function():
    """Clean up database before each test"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# Test User Registration
def test_register_success():
    """Test successful user registration"""
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "Test1234"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["email"] == "test@example.com"

def test_register_duplicate_email():
    """Test registration with duplicate email"""
    # First registration
    client.post("/auth/register", json={"email": "test@example.com", "password": "Test1234"})
    
    # Second registration with same email
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "Test1234"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_register_invalid_email():
    """Test registration with invalid email format"""
    response = client.post("/auth/register", json={"email": "invalid-email", "password": "Test1234"})
    assert response.status_code == 422

def test_register_weak_password_short():
    """Test registration with password too short"""
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "Test1"})
    assert response.status_code == 422
    assert "Password must be at least 8 characters long" in str(response.json())

def test_register_weak_password_no_uppercase():
    """Test registration with password missing uppercase"""
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "test1234"})
    assert response.status_code == 422
    assert "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number" in str(response.json())

def test_register_weak_password_no_lowercase():
    """Test registration with password missing lowercase"""
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "TEST1234"})
    assert response.status_code == 422
    assert "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number" in str(response.json())

def test_register_weak_password_no_digit():
    """Test registration with password missing digit"""
    response = client.post("/auth/register", json={"email": "test@example.com", "password": "TestTest"})
    assert response.status_code == 422
    assert "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter and one number" in str(response.json())

def test_register_missing_fields():
    """Test registration with missing required fields"""
    response = client.post("/auth/register", json={"email": "test@example.com"})
    assert response.status_code == 422

# Test User Login
def test_login_success():
    """Test successful user login"""
    # First register a user
    client.post("/auth/register", json={"email": "test@example.com", "password": "Test1234"})
    
    # Then test login
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "Test1234"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_email():
    """Test login with non-existent email"""
    response = client.post("/auth/login", json={"email": "nonexistent@example.com", "password": "Test1234"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

def test_login_invalid_password():
    """Test login with wrong password"""
    # First register a user
    client.post("/auth/register", json={"email": "test@example.com", "password": "Test1234"})
    
    # Then test login with wrong password
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "WrongPassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

def test_login_missing_fields():
    """Test login with missing required fields"""
    response = client.post("/auth/login", json={"email": "test@example.com"})
    assert response.status_code == 422

# Test JWT Token
def test_jwt_token_structure():
    """Test JWT token contains expected fields"""
    # Register and login
    client.post("/auth/register", json={"email": "test@example.com", "password": "Test1234"})
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "Test1234"})
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "token_type" in data
    assert data["token_type"] == "bearer"
    
    # Token should be a non-empty string
    assert isinstance(data["access_token"], str)
    assert len(data["access_token"]) > 0

def test_jwt_token_verification():
    """Test JWT token can be verified"""
    from src.utils.auth import verify_jwt
    
    # Register and login
    client.post("/auth/register", json={"email": "test@example.com", "password": "Test1234"})
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "Test1234"})
    
    token = response.json()["access_token"]
    payload = verify_jwt(token)
    assert "id" in payload
    assert isinstance(payload["id"], int)

def test_jwt_token_invalid():
    """Test JWT token verification with invalid token"""
    from src.utils.auth import verify_jwt
    from fastapi import HTTPException
    
    with pytest.raises(HTTPException) as exc_info:
        verify_jwt("invalid_token")
    
    assert exc_info.value.status_code == 401
    assert exc_info.value.detail == "Could not validate credentials"
