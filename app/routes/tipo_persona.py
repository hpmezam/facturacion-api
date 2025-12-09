from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db

from app.schemas.tipo_persona import (
    TipoPersonaCreate,
    TipoPersonaRead,
    TipoPersonaUpdate
)

from app.controllers.tipo_persona import (
    crearTipoPersona,
    obtenerTipoPersonas,
    obtenerTipoPersonaPorId,
    actualizarTipoPersona,
    eliminarTipoPersona
)

tipo_persona_router = APIRouter(prefix='/tipo_persona', tags=['Tipos de Persona'])

@tipo_persona_router.post('/', response_model=TipoPersonaRead)
def crear_tipo_persona(tipo_persona: TipoPersonaCreate, db: Session = Depends(get_db)):
    return crearTipoPersona(db, tipo_persona)

@tipo_persona_router.get('/', response_model=list[TipoPersonaRead])
def obtener_tipo_persona(db: Session = Depends(get_db)):
    return obtenerTipoPersonas(db)

@tipo_persona_router.get('/{id}', response_model=TipoPersonaRead)
def obtener_tipo_persona(id: int, db: Session = Depends(get_db)):
    return obtenerTipoPersonaPorId(db, id)

@tipo_persona_router.put('/{id}', response_model=TipoPersonaRead)
def actualizar_tipo_persona(id: int, tipo_persona: TipoPersonaUpdate, db: Session = Depends(get_db)):
    return actualizarTipoPersona(db, id, tipo_persona)

@tipo_persona_router.delete('/{id}', status_code=200)
def eliminar_tipo_persona(id: int, session: Session = Depends(get_db)):
    return eliminarTipoPersona(session, id) 