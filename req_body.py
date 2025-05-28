import uvicorn
from fastapi import FastAPI, Body
from typing import List
from pydantic import BaseModel, Field


app = FastAPI()

# @app.post("/students")
# async def student_data(name:str=Body(...),
# marks:int=Body(...)):
#    return {"name":name,"marks": marks}

class Student(BaseModel):
   id: int
   name :str = Field(None, title="name of student", max_length=10)
   subjects: List[str] = []
@app.post("/students/")
async def student_data(s1: Student):
   return s1

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}

@app.post("/students/{college}")
async def student_data(college:str, age:int, student:Student):
   retval={"college":college, "age":age, **student.model_dump()}
   return retval