# src/main.py
from fastapi import FastAPI
from src.routers import auth

app = FastAPI(title="TODO Management API", version="1.0.0")

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to TODO Management API"}
