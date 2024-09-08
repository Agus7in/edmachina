from pydantic import BaseModel

class LeadCreate(BaseModel):
    nombre_completo: str
    direccion: str
    telefono: str
    email: str

class LeadResponse(BaseModel):
    id_lead: int
    nombre_completo: str
    direccion: str
    telefono: str
    email: str

class InscripcionCreate(BaseModel):
    lead_id: int
    materia_id: int
    carrera_id: int
    anio_inscripcion: int
    nro_veces_cursada: int
    tiempo_cursado: str

class InscripcionResponse(BaseModel):
    id_inscripcion: int
    lead_id: int
    materia_id: int
    carrera_id: int
    anio_inscripcion: int
    nro_veces_cursada: int
    tiempo_cursado: str

class Config:
    orm_mode = True

class MateriaResponse(BaseModel):
    id_materia: int
    nombre_materia: str

class CarreraResponse(BaseModel):
    id_carrera: int
    nombre_carrera: str