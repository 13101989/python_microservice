from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hell on World"}

def test_read_data():
    response = client.get("/data/ion")
    assert response.status_code == 200
    assert response.json() == {"message": "Hell on World ion"}