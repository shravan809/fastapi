<<<<<<< HEAD
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
async def fun():
    return {'name':'shravan','age':27}

@app.get('/items/')
async def list_items():
    return {"car":"Benz",'model':2018}

@app.get('/blog/unpublished/')
def unpublished():
    return {"data":"all unpublised bolg"}

@app.get('/blog/')
def index(limit,published:bool=True,sort:Optional[str]=None):
    if published:
        return {"data":f"{limit} published blogs from the db"}
    else:
        return {"data":f"{limit} blogs from the db"}

@app.get('/blog/{id}')
def blog(id:int):
    return {"data":id}

@app.get('/blog/{id}/comments/')
def comments(id:int,limit):
    #return limit
    return {"data":['1','2']}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog/')
def create_blog(blog:Blog):
    
    return {'data':f'blog is created with title as {blog.title}'}
=======
from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def fun():
    return {'name':'shravan','age':27}

@app.get('/items/')
async def list_items():
    return {"car":"Benz",'model':2018}
>>>>>>> f2d2179ea9b6ef5bde189c4692b3086a3d38ee67
