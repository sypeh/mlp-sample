from fastapi import FastAPI

from sample.routers import named_entity
from sample.routers import proofreading

app = FastAPI()

app.include_router(named_entity.router)
app.include_router(proofreading.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}