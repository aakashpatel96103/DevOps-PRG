from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_employee_requires_authentication():
    response = client.get("/employees/")
    assert response.status_code == 403
