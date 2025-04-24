from fastapi import FastAPI, Depends, Response, status, HTTPException
from . import schemas, model,hashing
from .database import engine, get_db
from sqlalchemy.orm import Session
from typing import List


model.Base.metadata.create_all(engine)

app = FastAPI()



@app.post("/blog", response_model=schemas.ShowBlog)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = model.Blog(title=request.title, body=request.body, published=request.published,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs

@app.get("/blog/{id}", response_model=schemas.ShowBlog)
def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
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

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
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



@app.post("/user", response_model=schemas.ShowUser,tags=["User"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    
    new_user = model.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user/{id}", response_model=schemas.ShowUser,tags=["User"])
def get_user(id,db:Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    return user