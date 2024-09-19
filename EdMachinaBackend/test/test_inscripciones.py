import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_create_inscripcion():
    response = client.post("/inscripciones", json={"lead_id": 4,"materia_id": 1, "carrera_id": 1, "anio_inscripcion": 2024, "nro_veces_cursada": 1, "tiempo_cursado": "1 semestre"})
    assert response.status_code == 201
    assert "lead_id" in response.json()
    assert "materia_id" in response.json()
    assert response.json()["materia_id"] == 1
    assert "carrera_id" in response.json()
    assert response.json()["carrera_id"] == 1
    assert "anio_inscripcion" in response.json()
    assert response.json()["anio_inscripcion"] == 2024
    assert "nro_veces_cursada" in response.json()
    assert response.json()["nro_veces_cursada"] == 1
    assert "tiempo_cursado" in response.json()
    assert response.json()["tiempo_cursado"] == "1 semestre"
    
def test_get_inscripcion():
    response = client.get("/inscripciones")
    assert response.status_code == 200
    inscripciones = response.json()
    assert isinstance(inscripciones, list)
    assert len(inscripciones) > 0
    
def test_get_inscripcion_by_id():
    response = client.get("/inscripciones/16")
    print(response)
    assert response.status_code == 200
    inscripcion = response.json()
    assert isinstance(inscripcion, dict)
    assert "lead_id" in inscripcion
    assert "materia_id" in inscripcion
    assert "carrera_id" in inscripcion
    assert "anio_inscripcion" in inscripcion
    assert "nro_veces_cursada" in inscripcion
    assert "tiempo_cursado" in inscripcion