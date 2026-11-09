from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

notes = []

class Note(BaseModel):
    title: str
    content: str

@app.post("/notes")
def create_note(note: Note):
    notes.append(note)
    return {"id": len(notes) - 1, "note": note}

@app.get("/notes")
def get_all_notes():
    return notes

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]