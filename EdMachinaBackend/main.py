from fastapi import FastAPI
from leads import lead_service
from inscripciones import inscripcion_service
from materias import materias_service
from carreras import carreras_service

app = FastAPI()

app.include_router(lead_service, prefix="/leads")
app.include_router(inscripcion_service, prefix="/inscripciones")
app.include_router(materias_service, prefix="/materias")
app.include_router(carreras_service, prefix="/carreras")