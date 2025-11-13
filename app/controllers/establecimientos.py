from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.establecimientos import Establecimiento
from app.models.empresas import Empresa
from app.schemas.establecimientos import (
    EstablecimientoCreate,
    EstablecimientoRead,
    EstablecimientoUpdate,
)
# Crear un nuevo establecimiento
def crearEstablecimiento(db: Session, establecimiento: EstablecimientoCreate) -> EstablecimientoRead:
    empresa = db.get(Empresa, establecimiento.empresa_id)
    if not empresa:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La empresa con ID {establecimiento.empresa_id} no existe."
        )
    nuevo = Establecimiento(**establecimiento.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
def obtenerEstablecimientos(db: Session) -> list[EstablecimientoRead]:
    return db.exec(select(Establecimiento)).all()
def obtenerEstablecimientoPorId(db: Session, id: int) -> EstablecimientoRead:
    establecimiento = db.get(Establecimiento, id)
    if not establecimiento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Establecimiento con id '{id}' no encontrado.")
    return establecimiento
def actualizarEstablecimiento(db: Session, id: int, establecimiento: EstablecimientoUpdate) -> EstablecimientoRead:
    existente = db.get(Establecimiento, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Establecimiento con id '{id}' no encontrado.")
    
    datos_por_actualizar = establecimiento.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar el establecimiento.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente
def eliminarEstablecimiento(db: Session, id: int) -> None:
    establecimiento = db.get(Establecimiento, id)
    if not establecimiento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Establecimiento con id '{id}' no encontrado.")
    db.delete(establecimiento)
    db.commit()
    return {"detail": f"Establecimiento con id '{id}' eliminado correctamente."}