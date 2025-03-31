from http.server import BaseHTTPRequestHandler
import json
import urllib.parse

def handler(request, response):
    # Get the request method
    method = request.get("method", "")
    
    # Parse query parameters
    query = request.get("query", {})
    names = query.get("name", [])
    
    if method == "POST":
        # Get data from request body
        data = json.loads(request.get("body", "{}"))
    else:  # GET
        # Use default data or load from another source
        data = [
            {"name": "John", "marks": 85},
            {"name": "Alice", "marks": 92},
            {"name": "Bob", "marks": 78}
        ]
    
    # Process the data
    result = {"marks": []}
    for name in names:
        for entry in data:
            if entry["name"] == name:
                result["marks"].append(entry["marks"])
    
    # Return the response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(result)
    }

