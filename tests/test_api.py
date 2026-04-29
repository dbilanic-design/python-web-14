from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_contacts():
    response = client.get("/contacts")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
