from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert data["service"] == "devopsjr-api-cicd"
    assert data["version"] == "0.1.0"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "devopsjr-api-cicd",
    }


def test_info():
    response = client.get("/info")
    assert response.status_code == 200

    data = response.json()
    assert data["project"] == "devopsjr-api-cicd"
    assert data["version"] == "0.1.0"
    assert "environment" in data
    assert "timestamp" in data