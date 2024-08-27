from sqlalchemy import Column,Integer,String, ForeignKey
from .database import Base

class Book(Base):
    __tablename__='book'
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String)
    

class Author(Base):
    __tablename__='author'
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String)
    