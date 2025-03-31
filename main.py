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
        # Load data from q-vercel-python.json
        with open('q-vercel-python.json') as f:
            data = json.load(f)
    
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
