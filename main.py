from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from typing import List, Optional

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

# GET endpoint
@app.get("/api/marks")
async def get_marks(name: Optional[List[str]] = None):
    # Load data from file
    data = load_data()
    
    # If name parameter is not provided
    if not name:
        return {"marks": []}
    
    # Process the data
    result = {"marks": []}
    for n in name:
        for entry in data:
            if entry.get("name") == n:
                result["marks"].append(entry.get("marks"))
    
    return result

# POST endpoint
@app.post("/api/marks")
async def post_marks(request: Request, name: Optional[List[str]] = None):
    try:
        # Get data from request body
        body = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    # If name parameter is not provided
    if not name:
        return {"marks": []}
    
    # Process the data
    result = {"marks": []}
    for n in name:
        for entry in body:
            if entry.get("name") == n:
                result["marks"].append(entry.get("marks"))
    
    return result

# For local developmen
