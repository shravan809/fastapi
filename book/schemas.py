from pydantic import BaseModel

class Book(BaseModel):
    name:str
    


class Author(BaseModel):
    name:str
    