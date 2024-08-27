from fastapi import FastAPI
from . import models
from .database import engine
from .routers import book,author

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(book.router)
app.include_router(author.router)
