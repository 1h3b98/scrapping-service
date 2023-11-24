from fastapi.testclient import TestClient
from src.main import app  # Replace with your actual FastAPI app

client = TestClient(app)

def test_retrieve_posts():
    response = client.get("/", params={"page_id": "some_page_id", "limit_pages": 2})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_store_posts_success():
    response = client.get("/", params={"page_id": "some_page_id", "limit_pages": 2, "storage": True})
    assert response.status_code == 200
    assert response.text == "data saved into database"

def test_store_posts_failure():
    # You'll need to mock or manipulate the environment so that the database insertion fails
    response = client.get("/", params={"page_id": "some_page_id", "limit_pages": 2, "storage": True})
    assert response.status_code == 200
    assert response.text == "error"
