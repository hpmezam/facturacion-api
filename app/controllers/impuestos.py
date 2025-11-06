from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.impuestos import Impuesto
from app.schemas.impuestos import (
    ImpuestoCreate,
    ImpuestoRead,
    ImpuestoUpdate,
)

def crearImpuesto(db: Session, impuesto: ImpuestoCreate) -> ImpuestoRead:
    nuevo_impuesto = Impuesto(**impuesto.model_dump())
    db.add(nuevo_impuesto)
    db.commit()
    db.refresh(nuevo_impuesto)
    return nuevo_impuesto   

def obtenerImpuestos(db: Session) -> list[ImpuestoRead]:
    return db.exec(select(Impuesto)).all()

def obtenerImpuestoPorId(db: Session, id: int) -> ImpuestoRead:
    impuesto = db.get(Impuesto, id)
    if not impuesto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Impuesto con id '{id}' no encontrado.")
    return impuesto

def actualizarImpuesto(db: Session, id: int, impuesto: ImpuestoUpdate) -> ImpuestoRead:
    existente = db.get(Impuesto, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Impuesto con id '{id}' no encontrado.")
    
    datos_por_actualizar = impuesto.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar el impuesto.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente

def eliminarImpuesto(db: Session, id: int) -> dict:
    impuesto = db.get(Impuesto, id)
    if not impuesto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Impuesto con id '{id}' no encontrado.")
    db.delete(impuesto)
    db.commit()
    return {"detail": f"Impuesto con id '{id}' eliminado correctamente."}
