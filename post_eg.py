import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Student API"}


class Student(BaseModel):
   id: int
   name :str = Field(None, title="name of student", max_length=10)
   subjects: List[str] = []

   
@app.post("/students/")
async def student_data(s1: Student):
   return s1