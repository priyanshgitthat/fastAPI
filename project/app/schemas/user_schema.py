


from pydantic import BaseModel,Field
from typing import List,Optional

class CreateUser(BaseModel):
    name:str = Field(...,min_length=1,max_length=100)
    username:str = Field(...,min_length=1,max_length=100)
    password:str = Field(...,min_length=6,max_length=100)

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    id:int
    name:str
    username:str 

    class Config:
        orm_mode = True



class LoginUser(BaseModel):
    username : str
    password : str

    class Config:
        orm_mode = True