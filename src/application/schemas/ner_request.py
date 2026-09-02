from pydantic import BaseModel

class NERRequest(BaseModel):
    text: str