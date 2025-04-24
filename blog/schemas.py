from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True

class ShowBlog(Blog):
    title: str
    published: bool
    class Config():
        from_attributes = True
       

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    class Config:
        from_attributes = True
