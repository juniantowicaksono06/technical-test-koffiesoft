# schemas.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: str
    name: str
    username: str

    class Config:
        orm_mode = True
