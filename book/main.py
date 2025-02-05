from fastapi import FastAPI
from . import models
from .database import engine
from .routers import book,author
from fastapi.middleware.cors import CORSMiddleware 

app=FastAPI()


origins = [
    "http://localhost:3000",
    "http://localhost:4000"    
]
 
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


models.Base.metadata.create_all(engine)

app.include_router(book.router)
app.include_router(author.router)
