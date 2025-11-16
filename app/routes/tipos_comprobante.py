from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.tipos_comprobante import (
    TipoComprobanteCreate,
    TipoComprobanteRead,
    TipoComprobanteUpdate,
)
from app.controllers.tipos_comprobante import (
    crearTipoComprobante,
    obtenerTiposComprobante,
    obtenerTipoComprobanteporId,
    actualizarTipoComprobante,
)
tipos_comprobante_router = APIRouter(prefix='/tipos_comprobante', tags=['Tipos Comprobante'])
@tipos_comprobante_router.post('/', response_model=TipoComprobanteRead)
def crear_tipo_comprobante(tipo: TipoComprobanteCreate, db: Session = Depends(get_db)):
    return crearTipoComprobante(db, tipo)
@tipos_comprobante_router.get('/', response_model=list[TipoComprobanteRead])
def obtener_tipos_comprobante(db: Session = Depends(get_db)):
    return obtenerTiposComprobante(db)
@tipos_comprobante_router.get('/{id}', response_model=TipoComprobanteRead)
def obtener_tipo_comprobante_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerTipoComprobanteporId(db, id)
@tipos_comprobante_router.put('/{id}', response_model=TipoComprobanteRead)
def actualizar_tipo_comprobante(id: int, tipo: TipoComprobanteUpdate, db: Session = Depends(get_db)):
    return actualizarTipoComprobante(db, id, tipo)
