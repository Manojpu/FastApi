from pydantic import BaseModel
from typing import Optional

class BlogBase(BaseModel):
    title: str
    body: str
    published: Optional[bool] = True
   
class Blog(BlogBase):
     class Config:
        form_attribute = True


       

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: list[Blog] = []
    class Config:
        from_attributes = True

class ShowBlog(Blog):
    title: str
    published: bool
    creater: ShowUser
    class Config():
        from_attributes = True
