import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_endpoint():
    """Test the hello endpoint with a valid name."""
    response = client.get("/hello/World")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_hello_endpoint_with_special_characters():
    """Test the hello endpoint with special characters in name."""
    response = client.get("/hello/Test%20User")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Test User!"}

def test_hello_endpoint_empty_name():
    """Test the hello endpoint with empty name."""
    response = client.get("/hello/")
    assert response.status_code == 404

def test_cors_headers():
    """Test that CORS headers are properly set."""
    response = client.options("/hello/Test")
    assert response.status_code == 200

def test_api_docs_endpoint():
    """Test that API documentation is accessible."""
    response = client.get("/docs")
    assert response.status_code == 200

def test_openapi_schema():
    """Test that OpenAPI schema is accessible."""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Hello API"
    assert data["version"] == "1.0.0"
