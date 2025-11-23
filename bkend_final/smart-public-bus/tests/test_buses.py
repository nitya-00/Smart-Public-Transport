from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_buses():
    response = client.get("/buses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_bus_crowd():
    bus_id = 1  # Example bus ID
    response = client.get(f"/buses/{bus_id}/crowd")
    assert response.status_code == 200
    assert "crowd_level" in response.json()

def test_get_bus_eta():
    bus_id = 1  # Example bus ID
    response = client.get(f"/buses/{bus_id}/eta")
    assert response.status_code == 200
    assert "eta" in response.json()

def test_get_bus_telemetry():
    bus_id = 1  # Example bus ID
    response = client.get(f"/buses/{bus_id}/telemetry")
    assert response.status_code == 200
    assert "gps_data" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}