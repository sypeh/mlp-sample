from fastapi import FastAPI
from pydantic import BaseModel

from sample.routers import named_entity

# class Item(BaseModel):
#     text: str

app = FastAPI()

app.include_router(named_entity.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.post("/proofreading")
# def proofreading(item: Item):
#     return {"Hello": "World"}