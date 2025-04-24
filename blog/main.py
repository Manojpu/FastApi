from fastapi import FastAPI
from . import model
from .database import engine


from .routers import blog, user

model.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)






