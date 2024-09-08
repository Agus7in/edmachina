from typing import List
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import Inscripcion
from db import get_db
import schemas

inscripcion_service = APIRouter()

@inscripcion_service.get("/", response_model=List[schemas.InscripcionResponse], status_code=200)
async def inscripciones(db: Session = Depends(get_db)):
    inscripciones = db.query(Inscripcion).all()
    return inscripciones

@inscripcion_service.get("/{id:int}", response_model=schemas.InscripcionResponse, status_code=200)
async def inscripcion_by_id(id: int, db: Session = Depends(get_db)):
    inscripcion =  db.query(Inscripcion).filter(Inscripcion.id_inscripcion == id).first()
    if inscripcion is None:
        raise NoResultFound(status_code=404, detail=f"No se encontro una inscripcion con el id: {id}")
    return inscripcion

@inscripcion_service.post("/", response_model=schemas.InscripcionResponse, status_code=201)
async def create_inscripcion(inscripcion: schemas.InscripcionCreate, db: Session = Depends(get_db)):
    inscripcion = Inscripcion(
        lead_id = inscripcion.lead_id,
        materia_id = inscripcion.materia_id,
        carrera_id = inscripcion.carrera_id,
        anio_inscripcion = inscripcion.anio_inscripcion,
        nro_veces_cursada = inscripcion.nro_veces_cursada,
        tiempo_cursado = inscripcion.tiempo_cursado
    )
    db.add(inscripcion)
    db.commit()
    db.refresh(inscripcion)
    return inscripcion