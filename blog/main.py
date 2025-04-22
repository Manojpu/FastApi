from fastapi import FastAPI
from .import schemas,model
from database import engine

model.Base.metadata.create_all(engine)
app = FastAPI()

@app.post("/blog")
def create_blog(request: schemas.Blog):
    return schemas.Blog