# app/schemas/admin_schema.py

from pydantic import BaseModel

class AdminCreate(BaseModel):
    name: str
    username: str
    password: str

    class Config:
        orm_mode = True


class AdminLogin(BaseModel):
    username:str
    password:str

    class Config:
        orm_mode = True