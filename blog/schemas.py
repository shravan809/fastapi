from pydantic import BaseModel

class User(BaseModel):
    name:str
    email:str
    password:str


class ShowUser(BaseModel):
    name:str
    email:str

    class Config():
        from_attributes=True

class Blog(BaseModel):
    title:str
    body:str
    user_id:int

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        from_attributes=True


class Login(BaseModel):
    username:str
    password:str