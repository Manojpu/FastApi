from fastapi import  Depends, HTTPException, status
from .. import schemas, model, hashing
from sqlalchemy.orm import Session
from ..database import get_db

def create_user(request: schemas.User,db: Session = Depends(get_db)):
    new_user = model.User(name=request.name, email=request.email, password=hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    return user