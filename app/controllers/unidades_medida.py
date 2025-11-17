from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.unidades_medida import UnidadMedida
from app.schemas.unidades_medida import (
    UnidadMedidaCreate,
    UnidadMedidaRead,
    UnidadMedidaUpdate,
)

def crearUnidadMedida(db: Session, unidad_medida: UnidadMedidaCreate) -> UnidadMedidaRead:
    nueva_unidad_medida = UnidadMedida(**unidad_medida.model_dump())
    db.add(nueva_unidad_medida)
    db.commit()
    db.refresh(nueva_unidad_medida)
    return nueva_unidad_medida

def obtenerUnidadesMedida(db: Session) -> list[UnidadMedidaRead]:
    return db.exec(select(UnidadMedida)).all()

def obtenerUnidadMedidaPorId(db: Session, id: int) -> UnidadMedidaRead:
    unidad_medida = db.get(UnidadMedida, id)
    if not unidad_medida:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unidad de medida con id '{id}' no encontrada.")
    return unidad_medida

def actualizarUnidadMedida(db: Session, id: int, unidad_medida: UnidadMedidaUpdate) -> UnidadMedidaRead:   
    existente = db.get(UnidadMedida, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unidad de medida con id '{id}' no encontrada.")
    
    datos_por_actualizar = unidad_medida.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar la unidad de medida.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente

def eliminarUnidadMedida(db: Session, id: int) -> dict:
    unidad_medida = db.get(UnidadMedida, id)
    if not unidad_medida:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Unidad de medida con id '{id}' no encontrada.")
    db.delete(unidad_medida)
    db.commit()
    return {"detail": f"Unidad de medida con id '{id}' eliminada correctamente."}

