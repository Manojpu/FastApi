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
        orm_mode = True
