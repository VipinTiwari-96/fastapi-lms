from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List


router= APIRouter()

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

    
users= []

@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.get("/users/{id}")
async def get_user(id:int):
    return users[id]


@router.post("/users")
async def create_user(user:User):
    users.append(user)
    return 'success'