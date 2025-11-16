from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.tipos_comprobante import TipoComprobante
from app.schemas.tipos_comprobante import (
    TipoComprobanteCreate,
    TipoComprobanteRead,
    TipoComprobanteUpdate,
)
# Crear un nuevo tipo de comprobante
def crearTipoComprobante(db: Session, tipo: TipoComprobanteCreate) -> TipoComprobanteRead:
    nuevo = TipoComprobante(**tipo.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
def obtenerTiposComprobante(db: Session) -> list[TipoComprobanteRead]:
    return db.exec(select(TipoComprobante)).all()
def obtenerTipoComprobanteporId(db: Session, id: int) -> TipoComprobanteRead:
    tipo = db.get(TipoComprobante, id)
    if not tipo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tipo de comprobante con id '{id}' no encontrado.")
    return tipo
def actualizarTipoComprobante(db: Session, id: int, tipo: TipoComprobanteUpdate) -> TipoComprobanteRead:
    existente = db.get(TipoComprobante, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tipo de comprobante con id '{id}' no encontrado.")
    
    datos_por_actualizar = tipo.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar el tipo de comprobante.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente
