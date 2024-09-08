from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lead(Base):
    __tablename__ = 'leads'
    
    id_lead = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre_completo = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Materia(Base):
    __tablename__ = 'materias'
    
    id_materia = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre_materia = Column(String, nullable=False)

class Carrera(Base):
    __tablename__ = 'carreras'
    
    id_carrera = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre_carrera = Column(String, nullable=False)

class Inscripcion(Base):
    __tablename__ = 'inscripciones'
    
    id_inscripcion = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    lead_id = Column(Integer, ForeignKey('leads.id_lead'), nullable=False)
    materia_id = Column(Integer, ForeignKey('materias.id_materia'), nullable=False)
    carrera_id = Column(Integer, ForeignKey('carreras.id_carrera'), nullable=False)
    anio_inscripcion = Column(Integer, nullable=False)
    nro_veces_cursada = Column(Integer, nullable=False)
    tiempo_cursado = Column(String, nullable=False)