from typing import List
from fastapi import APIRouter
import sample.schemas.proofreading as proofreading

router = APIRouter()

@router.post("/proofreading")
def proofreading(request: proofreading.Request):
    return {"Hello": "World"}