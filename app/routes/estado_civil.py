from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db

from app.schemas.estado_civil import (
    EstadoCivilCreate,
    EstadoCivilRead,
    EstadoCivilUpdate
)

from app.controllers.estado_civil import (
    crearEstadoCivil,
    obtenerEstadosCiviles,
    obtenerEstadoCivilPorId,
    actualizarEstadoCivil,
    eliminarEstadoCivil
)

estado_civil_router = APIRouter(
    prefix="/estado_civil",
    tags=["Estado Civil"]
)

@estado_civil_router.post("/", response_model=EstadoCivilRead)
def crear_estado_civil(estado: EstadoCivilCreate, db: Session = Depends(get_db)):
    return crearEstadoCivil(db, estado)


@estado_civil_router.get("/", response_model=list[EstadoCivilRead])
def obtener_estados_civiles(db: Session = Depends(get_db)):
    return obtenerEstadosCiviles(db)


@estado_civil_router.get("/{id}", response_model=EstadoCivilRead)
def obtener_estado_civil(id: int, db: Session = Depends(get_db)):
    return obtenerEstadoCivilPorId(db, id)


@estado_civil_router.put("/{id}", response_model=EstadoCivilRead)
def actualizar_estado_civil(id: int, estado: EstadoCivilUpdate, db: Session = Depends(get_db)):
    return actualizarEstadoCivil(db, id, estado)


@estado_civil_router.delete("/{id}", status_code=200)
def eliminar_estado_civil(id: int, db: Session = Depends(get_db)):
    return eliminarEstadoCivil(db, id)