from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import json

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Function to load data from file
def load_data():
    try:
        with open('q-vercel-python.json') as f:
            return json.load(f)
    except FileNotFoundError:
        # Return empty list if file not found
        return []
    except json.JSONDecodeError:
        # Return empty list if JSON is invalid
        return []

# Load student data
students = {item["name"]: item["marks"] for item in load_data()}

# GET endpoint
@app.get("/api")
async def get_marks(name: List[str] = Query(...)):
    return {"marks": [students.get(n, 0) for n in name]}

# POST endpoint
@app.post("/api/marks")
async def post_marks(request: Request, name: Optional[List[str]] = None):
    try:
        # Get data from request body
        body = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    if not name:
        return {"marks": []}
    
    result = {"marks": []}
    for n in name:
        for entry in body:
            if entry.get("name") == n:
                result["marks"].append(entry.get("marks"))
    
    return result

# For local developmen
