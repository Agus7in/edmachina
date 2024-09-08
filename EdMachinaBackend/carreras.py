
from typing import List
from fastapi import APIRouter, Depends
from pytest import Session
from models import Carrera
from db import get_db
import schemas

carreras_service = APIRouter()

@carreras_service.get("/", response_model=List[schemas.CarreraResponse], status_code=200)
async def carreras(db: Session = Depends(get_db)):
    carreras = db.query(Carrera).all()
    return carreras