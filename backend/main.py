from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from pydantic import BaseModel
from typing import Dict

# Create FastAPI application instance
app = FastAPI(
    title="Hello API",
    description="A simple FastAPI serverless application for Netlify Functions",
    version="1.0.0"
)

# Configure CORS middleware to allow requests from any origin
# This is crucial for frontend applications to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for frontend integration
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Response model for consistent JSON structure
class HelloResponse(BaseModel):
    message: str

@app.get("/hello/{name}", response_model=HelloResponse)
async def hello_name(name: str) -> HelloResponse:
    """
    GET endpoint that returns a personalized greeting message.
    
    Args:
        name (str): The name to include in the greeting message
        
    Returns:
        HelloResponse: JSON response with greeting message
    """
    return HelloResponse(message=f"Hello, {name}!")

# Serverless wrapper for Netlify Functions
# Mangum is used to make FastAPI compatible with AWS Lambda/Netlify Functions
handler = Mangum(app, lifespan="off")
