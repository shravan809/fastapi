from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models
from sqlalchemy.orm import Session
from ..hashing import Hash
from passlib.context import CryptContext

router=APIRouter(tags=['Authentication'])
pwd_cxt=CryptContext(schemes=['bcrypt'],deprecated='auto')


@router.post('/login')
def login(request:schemas.Login,db:Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='user not found')

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='incorrect password')
    return user

