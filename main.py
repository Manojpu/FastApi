from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"data":{
        "name": "Pubudu",
        "age": 22,
        "country": "Sri Lanka"
    }}

@app.get("/about")
def about():
    return {"data":{
        "about": "I am a software engineer with a passion for learning new technologies and solving complex problems. I have experience in web development, data analysis, and machine learning. I enjoy working on projects that challenge me and allow me to grow as a developer."
    }}

@app.get("/blog/{id}")
def show(id):
    return {"data":id}