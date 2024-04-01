from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List


router= APIRouter()

class Course(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

    
courses= []

@router.get("/courses", response_model=List[Course])
async def get_courses():
    return {"courses":[]}


@router.get("/courses/{id}")
async def get_course(id:int):
    return {"courses":[]}


@router.post("/courses")
async def create_course(course:Course):
    return {"courses":[]}

@router.put("/courses/{id}")
async def update_course(course:Course):
    return {"courses":[]}


@router.delete("/courses/{id}")
async def delete_course(course:Course):
    return {"courses":[]}