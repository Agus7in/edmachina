from typing import List
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models import Lead
from db import get_db
import schemas

lead_service = APIRouter()

@lead_service.get("/", response_model=List[schemas.LeadResponse], status_code=200)
async def leads(db: Session = Depends(get_db)):
    leads = db.query(Lead).all()
    return leads

@lead_service.get("/{id:int}", response_model=schemas.LeadResponse, status_code=200)
async def lead_by_id(id: int, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id_lead == id).first()
    if lead is None:
        raise HTTPException(status_code=404, detail=f"No se encontró un Lead con el id: {id}")
    return lead

@lead_service.post("/", response_model=schemas.LeadResponse, status_code=201)
async def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    lead_to_insert = Lead(
        nombre_completo=lead.nombre_completo,
        direccion=lead.direccion,
        telefono=lead.telefono,
        email=lead.email
    )
    db.add(lead_to_insert)
    db.commit()
    db.refresh(lead_to_insert)
    return lead_to_insert

