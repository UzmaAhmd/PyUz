from fastapi import FastAPI
from typing import Union
import uvicorn


app = FastAPI()


@app.get("/")
async def index():
    return {"Message": "Hello World"}
# 
# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World"}
if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.0", port=8000, reload=True)

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def index():
#    return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}