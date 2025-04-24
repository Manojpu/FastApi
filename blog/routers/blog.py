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

@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs

@router.get("/{id}", response_model=schemas.ShowBlog)
def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    db.delete(blog)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog_query = db.query(model.Blog).filter(model.Blog.id == id)
    blog = blog_query.first()
    
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    
    blog_query.update(request.dict(), synchronize_session=False)
    db.commit()
    return {"message": f"Blog with id {id} updated successfully."}