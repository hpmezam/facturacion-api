from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.establecimientos import (
    EstablecimientoCreate,
    EstablecimientoRead,
    EstablecimientoUpdate,
)
from app.controllers.establecimientos import (
    crearEstablecimiento,
    obtenerEstablecimientos,
    obtenerEstablecimientoPorId,
    actualizarEstablecimiento,
    eliminarEstablecimiento,
)
establecimientos_router = APIRouter(prefix='/establecimientos', tags=['Establecimientos'])
@establecimientos_router.post('/', response_model=EstablecimientoRead)
def crear_establecimiento(establecimiento: EstablecimientoCreate, db: Session = Depends(get_db)):
    return crearEstablecimiento(db, establecimiento)
@establecimientos_router.get('/', response_model=list[EstablecimientoRead])
def obtener_establecimientos(db: Session = Depends(get_db)):
    return obtenerEstablecimientos(db)
@establecimientos_router.get('/{id}', response_model=EstablecimientoRead)
def obtener_establecimiento_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerEstablecimientoPorId(db, id)
@establecimientos_router.put('/{id}', response_model=EstablecimientoRead)
def actualizar_establecimiento(id: int, establecimiento: EstablecimientoUpdate, db: Session = Depends(get_db)):
    return actualizarEstablecimiento(db, id, establecimiento)
@establecimientos_router.delete('/{id}', status_code=204)
def eliminar_establecimiento(id: int, session: Session = Depends(get_db)):
    """
    Elimina un establecimiento por su ID.
    Retorna un mensaje de confirmación si se elimina correctamente.
    """
    return eliminarEstablecimiento(session, id)