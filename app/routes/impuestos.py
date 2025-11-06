from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db

from app.schemas.impuestos import (
    ImpuestoCreate,
    ImpuestoRead,
    ImpuestoUpdate
)

from app.controllers.impuestos import (
    crearImpuesto,
    obtenerImpuestoPorId,
    obtenerImpuestos,
    actualizarImpuesto,
    eliminarImpuesto
)

impuestos_router = APIRouter(prefix='/impuestos', tags=['Impuestos'])
@impuestos_router.post('/', response_model=ImpuestoRead)
def crear_impuesto(impuesto: ImpuestoCreate, db: Session = Depends(get_db)):
    return crearImpuesto(db, impuesto)

@impuestos_router.get('/', response_model=list[ImpuestoRead])
def obtener_impuestos(db: Session = Depends(get_db)):
    return obtenerImpuestos(db)

@impuestos_router.get('/{id}', response_model=ImpuestoRead)
def obtener_impuesto_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerImpuestoPorId(db, id)

@impuestos_router.put('/{id}', response_model=ImpuestoRead)
def actualizar_impuesto(id: int, impuesto: ImpuestoUpdate, db: Session = Depends(get_db)):
    return actualizarImpuesto(db, id, impuesto)

@impuestos_router.delete('/{id}', status_code=200)
def eliminar_impuesto(id: int, session: Session = Depends(get_db)):
    return eliminarImpuesto(session, id)

