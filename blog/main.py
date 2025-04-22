from fastapi import FastAPI, Depends, Response, status
from .import schemas,model
from .database import engine, SessioLocal
from sqlalchemy.orm import Session

model.Base.metadata.create_all(engine)
app = FastAPI()


def get_db():
    db = SessioLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
def create_blog(request: schemas.Blog,db:Session = Depends(get_db)):
    new_blog = model.Blog(title=request.title, body=request.body, published=request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog")
def get_blogs(db:Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs

@app.get("/blog/{id}")
def get_blog(id,response: Response,db:Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"Blog with id {id} not found"}
        
    return blog