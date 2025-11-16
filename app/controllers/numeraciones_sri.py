from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.numeraciones_sri import NumeracionSRI
from app.models.establecimientos import Establecimiento
from app.models.tipos_comprobante import TipoComprobante
from app.schemas.numeraciones_sri import (
    NumeracionSRICreate,
    NumeracionSRIRead,
    NumeracionSRIUpdate,
)
# Crear una nueva numeración SRI
def crearNumeracionSRI(db: Session, numeracion: NumeracionSRICreate) -> NumeracionSRIRead:
    establecimiento = db.get(Establecimiento, numeracion.establecimiento_id)
    if not establecimiento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El establecimiento con ID {numeracion.establecimiento_id} no existe."
        )
    tipoComprobante = db.get(TipoComprobante, numeracion.tipo_comprobante_id)
    if not tipoComprobante:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El tipo de comprobante con ID {numeracion.tipo_comprobante_id} no existe."
        )
    nueva = NumeracionSRI(**numeracion.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva
def obtenerNumeracionesSRI(db: Session) -> list[NumeracionSRIRead]:
    return db.exec(select(NumeracionSRI)).all()
def obtenerNumeracionSRIporId(db: Session, id: int) -> NumeracionSRIRead:
    numeracion = db.get(NumeracionSRI, id)
    if not numeracion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Numeración SRI con id '{id}' no encontrada.")
    return numeracion
def actualizarNumeracionSRI(db: Session, id: int, numeracion: NumeracionSRIUpdate) -> NumeracionSRIRead:
    existente = db.get(NumeracionSRI, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Numeración SRI con id '{id}' no encontrada.")
    
    datos_por_actualizar = numeracion.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar la numeración SRI.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente