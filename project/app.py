from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

# Initialize FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/hello/", response_class=HTMLResponse)
async def hello(request: Request, name:str):
   return templates.TemplateResponse("hello.html", {"request": request, "name":name})
