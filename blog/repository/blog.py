from .. import model
from fastapi import HTTPException, status 
from sqlalchemy.orm import Session
def get_all(db: Session):
    blogs = db.query(model.Blog).all()
    return blogs

def create(request: model.Blog, db: Session):
    new_blog = model.Blog(title=request.title, body=request.body, published=request.published,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



def get_blog_with_id(id: int, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog

def delete_blog(id: int, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    db.delete(blog)
    db.commit()
    return {"message": f"Blog with id {id} deleted successfully."}

def update_blog(id: int, request: model.Blog, db: Session):
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