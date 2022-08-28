from pydantic import BaseModel

class Todo(BaseModel):
    job : str