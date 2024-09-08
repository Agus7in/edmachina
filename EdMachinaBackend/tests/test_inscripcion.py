import pytest
from fastapi.testclient import TestClient
from EdMachinaBackend.inscripciones import inscripcion_service
from EdMachinaBackend.main import app
from EdMachinaBackend.models import Inscripcion
from EdMachinaBackend.db import get_db
from EdMachinaBackend.schemas import InscripcionCreate, InscripcionResponse

@pytest.fixture
def client():
    with TestClient(app, inscripcion_service) as client:
        yield client

@pytest.fixture
def db():
    db_session = next(get_db())
    try:
        yield db_session
    finally:
        db_session.close()

def create_inscripcion(db, **kwargs):
    inscripcion = Inscripcion(**kwargs)
    db.add(inscripcion)
    db.commit()
    db.refresh(inscripcion)
    return inscripcion

def test_get_inscripciones(client, db):
    inscripcion = create_inscripcion(db, lead_id=1, materia_id=1, carrera_id=1, anio_inscripcion=2022, nro_veces_cursada=1, tiempo_cursado="1 año")
    response = client.get("/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()["id_inscripcion"] == inscripcion.id_inscripcion

def test_get_inscripcion_by_id(client, db):
    inscripcion = create_inscripcion(db, lead_id=1, materia_id=1, carrera_id=1, anio_inscripcion=2022, nro_veces_cursada=1, tiempo_cursado="1 año")
    response = client.get(f"/{inscripcion.id_inscripcion}")
    assert response.status_code == 200
    assert response.json()["id_inscripcion"] == inscripcion.id_inscripcion

def test_create_inscripcion(client, db):
    inscripcion_create = InscripcionCreate(
        lead_id=1,
        materia_id=1,
        carrera_id=1,
        anio_inscripcion=2022,
        nro_veces_cursada=1,
        tiempo_cursado="1 año"
    )
    response = client.post("/", json=inscripcion_create.dict())
    assert response.status_code == 201
    assert response.json()["id_inscripcion"] == 1

def test_get_inscripcion_by_id_not_found(client, db):
    response = client.get("/100")
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontro una inscripcion con el id: 100"