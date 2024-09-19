import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)


def test_create_lead():
    response = client.post("/leads", json={"nombre_completo": "Agustin Martinez","direccion": "Ituzaingo 900", "telefono": "1234567890", "email": "amartinez@gmail.com"})
    assert response.status_code == 201
    assert "nombre_completo" in response.json()
    assert "direccion" in response.json()
    assert "telefono" in response.json()
    assert "email" in response.json()
    assert response.json()["nombre_completo"] == "Agustin Martinez"
    assert response.json()["direccion"] == "Ituzaingo 900"
    assert response.json()["telefono"] == "1234567890"
    assert response.json()["email"] == "amartinez@gmail.com"

def test_get_leads():
    response = client.get("/leads")
    assert response.status_code == 200
    leads = response.json()
    assert isinstance(leads, list)
    assert len(leads) > 0

def test_get_lead_by_id():
    response = client.get("/leads/4")
    assert response.status_code == 200
    lead = response.json()
    assert isinstance(lead, dict)
    assert "nombre_completo" in lead
    assert "direccion" in response.json()
    assert "telefono" in lead
    assert "email" in lead