from fastapi import FastAPI
from api import users, courses, sections

app = FastAPI()

app.include_router(users.router, tags=['Users'])
app.include_router(courses.router, tags=['Courses'])
app.include_router(sections.router, tags=['Sections'])

