from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Hello, your first API"}

# Path Parameters ("/users/5" pe jaoge to user_id = 5 milega)
@app.get("/users/{user_id}")
def home(user_id: int):
    return {"User ID": user_id, "Name": "Ayush"}

# Query Parameters (? ke baad wali cheeze)
@app.get("/search")
def search(q: str, limit: int = 10):
    return {"Query": q, "Limit": limit}

# Post Request (We use Pydantic model to define a basic structure of some Data)
from pydantic import BaseModel

class Note(BaseModel):
    title: str
    contents: str

@app.post("/notes")
def create_note(note: Note):
    return {"Message": "Note created successfully!", "Note": note}