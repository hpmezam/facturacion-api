from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.tipos_identificacion import (
    TipoIdentificacionCreate,
    TipoIdentificacionRead,
    TipoIdentificacionUpdate,
)
from app.controllers.tipos_identificacion import (
    crearTipoIdentificacion,
    obtenerTipoIdentificacions, obtenerTipoIdentificacionPorId, actualizarTipoIdentificacion, eliminarTipoIdentificacion
)

tipos_identificacion_router = APIRouter(prefix='/tipo_identificacion', tags=['Tipos de Identificación'])

@tipos_identificacion_router.post('/', response_model=TipoIdentificacionRead)
def crear_tipo_de_identificacion(tipoIdentificacion: TipoIdentificacionCreate, db: Session = Depends(get_db)):
    return crearTipoIdentificacion(db, tipoIdentificacion)

@tipos_identificacion_router.get('/', response_model=list[TipoIdentificacionRead])
def obtener_tipos_identificacion(db: Session = Depends(get_db)):
    return obtenerTipoIdentificacions(db)

@tipos_identificacion_router.get('/{id}', response_model=TipoIdentificacionRead)
def obtener_tipo_identificacion_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerTipoIdentificacionPorId(db, id)

@tipos_identificacion_router.put('/{id}', response_model=TipoIdentificacionRead)
def actualizar_tipo_identificacion(id: int, tipoIdentificacion: TipoIdentificacionUpdate, db: Session = Depends(get_db)):
    return actualizarTipoIdentificacion(db, id, tipoIdentificacion)

@tipos_identificacion_router.delete('/{id}', status_code=200)
def eliminar_tipo_identificacion(id: int, session: Session = Depends(get_db)):
    return eliminarTipoIdentificacion(session, id)