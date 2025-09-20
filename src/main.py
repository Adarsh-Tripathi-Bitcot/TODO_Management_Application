from fastapi import FastAPI
from src.routers import auth

app = FastAPI(title="TODO Management API", version="1.0.0")

# Including the authentication routes
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def read_root() -> dict:
    """
    Root endpoint that returns a welcome message.

    Returns:
        dict: A dictionary with a welcome message.
    """
    return {"message": "Welcome to TODO Management API"}
