from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client['notesdb']
notes_collection = db['notes']

class NoteIn(BaseModel):
    title: str
    text: str
    tags: Optional[List[str]] = []

@app.post("/notes/")
def create_note(note: NoteIn):
    result = notes_collection.insert_one(note.dict())
    return {"id": str(result.inserted_id)}

@app.get("/notes/")
def get_notes():
    notes = []
    for note in notes_collection.find():
        note["_id"] = str(note["_id"])
        notes.append(note)
    return notes
