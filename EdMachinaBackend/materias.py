from typing import List
from fastapi import APIRouter, Depends
from pytest import Session
from models import Materia
from db import get_db
import schemas

materias_service = APIRouter()

@materias_service.get("/", response_model=List[schemas.MateriaResponse], status_code=200)
async def materias(db: Session = Depends(get_db)):
    materias = db.query(Materia).all()
    return materias 