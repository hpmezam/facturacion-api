from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.tipos_identificacion import (
    TipoIdentificacionCreate,
    TipoIdentificacionRead,
    TipoIdentificacionUpdate,
)
from app.controllers.tipos_identificacion import (
    crear_tipo_identificacion,
    obtener_tipo_identificacions,
    obtener_tipo_identificacion_por_id,
    actualizar_tipo_identificacion,
    eliminar_tipo_identificacion
)

tipos_identificacion_router = APIRouter(prefix='/tipo_identificacion', tags=['Tipos de Identificación'])

@tipos_identificacion_router.post('/', response_model=TipoIdentificacionRead)
def crear_tipo_de_identificacion_endpoint(tipoIdentificacion: TipoIdentificacionCreate, db: Session = Depends(get_db)):
    return crear_tipo_identificacion(db, tipoIdentificacion)

@tipos_identificacion_router.get('/', response_model=list[TipoIdentificacionRead])
def obtener_tipos_identificacion_endpoint(db: Session = Depends(get_db)):
    return obtener_tipo_identificacions(db)

@tipos_identificacion_router.get('/{id}', response_model=TipoIdentificacionRead)
def obtener_tipo_identificacion_por_id_endpoint(id: int, db: Session = Depends(get_db)):
    return obtener_tipo_identificacion_por_id(db, id)

@tipos_identificacion_router.put('/{id}', response_model=TipoIdentificacionRead)
def actualizar_tipo_identificacion_endpoint(id: int, tipoIdentificacion: TipoIdentificacionUpdate, db: Session = Depends(get_db)):
    return actualizar_tipo_identificacion(db, id, tipoIdentificacion)

@tipos_identificacion_router.delete('/{id}', status_code=204)
def eliminar_tipo_identificacion_endpoint(id: int, session: Session = Depends(get_db)):
    """
    Elimina un tipo de identificación por su ID.
    Retorna un mensaje de confirmación si se elimina correctamente.
    """
    return eliminar_tipo_identificacion(session, id)