from fastapi import APIRouter, Depends
from typing import List
from ..import schemas, model, database
from sqlalchemy.orm import Session
router = APIRouter()

@router.get("/",response_model=List[schemas.ShowBlog],tags=["Blogs"])
def get_blogs_all(db: Session = Depends(database.get_db)):
    blogs = db.query(model.Blog).all()
    return blogs