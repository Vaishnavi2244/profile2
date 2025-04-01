from fastapi.test.client import TestClient
from app import app

def test_homepage():
    response = client.get("/")
    assert response.status_code == 200
    assert "<title>Index - iPortfolio Bootstrap Template</title>" in respose.text
    