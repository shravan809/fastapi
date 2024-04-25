from fastapi import FastAPI,Depends,status,Response,HTTPException
from .schemas import Blog,ShowBlog,User,ShowUser
from . import models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from .routers import blog,user,auth

app=FastAPI()

models.Base.metadata.create_all(engine)
print(models.Base.metadata.create_all(engine))

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)


