from fastapi import APIRouter, Depends, Response, status, HTTPException
from typing import List
from ..import schemas, model
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)
from ..database import get_db

@router.get("/",response_model=List[schemas.ShowBlog])
def get_blogs_all(db: Session = Depends(get_db)):

    return blog.get_all(db)

@router.post("/", response_model=schemas.ShowBlog)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.get("/{id}", response_model=schemas.ShowBlog)
def get_blog_with_id(id: int, response: Response, db: Session = Depends(get_db)):

    return blog.get_blog_with_id(id, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
  
    return blog.delete_blog(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update_blog(id, request, db)