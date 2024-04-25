from fastapi import APIRouter,Depends,status,HTTPException
from ..schemas import User,ShowUser
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..hashing import Hash

router=APIRouter(tags=['users'])


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/user',response_model=ShowUser)
def create_user(request:User,db:Session=Depends(get_db)):

    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user/{id}',response_model=ShowUser)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    return user