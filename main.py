from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student data
with open('q-vercel-python.json') as f:
    students = {item["name"]: item["marks"] for item in json.load(f)}

@app.get("/api")
async def get_marks(name: list[str] = Query(...)):
    return {"marks": [students.get(n, 0) for n in name]}
