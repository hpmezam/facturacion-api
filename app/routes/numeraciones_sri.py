from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.numeraciones_sri import (
    NumeracionSRICreate,
    NumeracionSRIRead,
    NumeracionSRIUpdate,
)
from app.controllers.numeraciones_sri import (
    crearNumeracionSRI,
    obtenerNumeracionesSRI,             
    obtenerNumeracionSRIporId,
    actualizarNumeracionSRI,
)
numeraciones_sri_router = APIRouter(prefix='/numeraciones_sri', tags=['Numeraciones SRI'])
@numeraciones_sri_router.post('/', response_model=NumeracionSRIRead)
def crear_numeracion_sri(numeracion: NumeracionSRICreate, db: Session = Depends(get_db)):
    return crearNumeracionSRI(db, numeracion)
@numeraciones_sri_router.get('/', response_model=list[NumeracionSRIRead])
def obtener_numeraciones_sri(db: Session = Depends(get_db)):
    return obtenerNumeracionesSRI(db)
@numeraciones_sri_router.get('/{id}', response_model=NumeracionSRIRead)
def obtener_numeracion_sri_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerNumeracionSRIporId(db, id)
@numeraciones_sri_router.put('/{id}', response_model=NumeracionSRIRead)
def actualizar_numeracion_sri(id: int, numeracion: NumeracionSRIUpdate, db: Session = Depends(get_db)):
    return actualizarNumeracionSRI(db, id, numeracion)
