from .. import model  
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