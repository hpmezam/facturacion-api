from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.unidades_medida import (
    UnidadMedidaCreate,
    UnidadMedidaRead,
    UnidadMedidaUpdate,
)

from app.controllers.unidades_medida import (
    crearUnidadMedida,
    obtenerUnidadesMedida,
    obtenerUnidadMedidaPorId,   
    actualizarUnidadMedida,
    eliminarUnidadMedida
)

unidades_medida_router = APIRouter(prefix='/unidades_medida', tags=['Unidades de Medida'])
@unidades_medida_router.post('/', response_model=UnidadMedidaRead)
def crear_unidad_medida(unidad_medida: UnidadMedidaCreate, db: Session = Depends(get_db)):
    return crearUnidadMedida(db, unidad_medida)

@unidades_medida_router.get('/', response_model=list[UnidadMedidaRead])
def obtener_unidades_medida(db: Session = Depends(get_db)):
    return obtenerUnidadesMedida(db)

@unidades_medida_router.get('/{id}', response_model=UnidadMedidaRead)
def obtener_unidad_medida_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerUnidadMedidaPorId(db, id)

@unidades_medida_router.put('/{id}', response_model=UnidadMedidaRead)
def actualizar_unidad_medida(id: int, unidad_medida: UnidadMedidaUpdate, db: Session = Depends(get_db)):
    return actualizarUnidadMedida(db, id, unidad_medida)

@unidades_medida_router.delete('/{id}', status_code=200)
def eliminar_unidad_medida(id: int, session: Session = Depends(get_db)):
    return eliminarUnidadMedida(session, id)

