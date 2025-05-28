import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"Path Parameters"}
@app.get("/hello/{name}")
async def hello(name):
   return {"name": name}