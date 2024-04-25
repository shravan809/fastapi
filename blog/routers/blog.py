from fastapi import APIRouter,Depends,status,Response,HTTPException
from ..schemas import Blog,ShowBlog
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router=APIRouter(
    prefix='/blog',
    tags=['Blog'])


@router.post('/',status_code=status.HTTP_201_CREATED)
def home(request:Blog,db:Session=Depends(get_db)):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/get',response_model=List[ShowBlog])
def all(db:Session=Depends(get_db)):
    all_blog=db.query(models.Blog).all()
    return all_blog

@router.get('/{id}',response_model=ShowBlog)
def get_id(id,response:Response,db:Session=Depends(get_db)):
    blog_1=db.query(models.Blog).filter(models.Blog.id==id).first()
    print(blog_1)
    if not blog_1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"detail":f"blog with this id {id} is not exists"}
    return blog_1

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')    
    blog.delete()
    db.commit()
    return 'done'


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id,request:Blog,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    blog.update({'title':'my title'})
    db.commit()
    return 'updated'