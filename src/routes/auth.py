from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.post("/login")
async def login():
    # login logic
    return {"message": "logged in successfuly"}