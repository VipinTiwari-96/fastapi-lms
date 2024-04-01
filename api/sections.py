from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List


router= APIRouter()

class Section(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

    
sections= []

@router.get("/sections/{id}", response_model=List[Section])
async def get_sections():
    return {"courses":[]}

@router.get("/sections/{id}/content-blocks")
async def get_section_content_blocks(id:int):
    return {"courses":[]}


@router.get("/content-blocks/{id}")
async def get_content_block(section:Section):
    return {"courses":[]}
