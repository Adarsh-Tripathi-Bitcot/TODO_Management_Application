from fastapi import FastAPI
from app.routers import auth, todos

app = FastAPI(title="TODO Management Application", version="1.0.0")

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(todos.router, prefix="/todos", tags=["TODOs"])

@app.get("/")
async def root():
    return {"message": "TODO Management API"}
