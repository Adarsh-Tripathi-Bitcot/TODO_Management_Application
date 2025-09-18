from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/register")
async def register():
    raise HTTPException(status_code=501, detail="To be implemented in Step 3")

@router.post("/login")
async def login():
    raise HTTPException(status_code=501, detail="To be implemented in Step 3")