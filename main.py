from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

    
users= []

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.get("/users/{id}")
async def get_user(id:int):
    return users[id]


@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return 'success'
