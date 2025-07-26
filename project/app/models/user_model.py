

from sqlalchemy import Column,Integer,String
from app.database.db import Base

class Users(Base):
    __tablename__ = "UserTable"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False,index=True)
    username = Column(String,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)
