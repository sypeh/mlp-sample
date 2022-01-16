from pydantic import BaseModel

class Request(BaseModel):
    text: str
    
class Response(BaseModel):
    text: str
    tag: str
    entity_type: str