from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"data":{
        "name": "Pubudu",
        "age": 22,
        "country": "Sri Lanka"
    }}

@app.get("/about")
def about(limit,ex,published,sort: Optional[str] = None):
    if published == "true":
       return {"data":{
        "about": f"{limit} {ex} I am a software engineer with a passion for learning new technologies and solving complex problems. I have experience in web development, data analysis, and machine learning. I enjoy working on projects that challenge me and allow me to grow as a developer."
    }}

    else:
        return{
            "data": f"{limit} unpublished blogs"
        }
    
@app.get("/blog/{id}")
def show(id: int):
    return {"data":id}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] 
@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog created with title {request.title} and body {request.body} and published status {request.published}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)