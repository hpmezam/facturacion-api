from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.empresas import Empresa
from app.schemas.empresas import (
    EmpresaCreate,
    EmpresaRead,
    EmpresaUpdate,
)
# Crear una nueva empresa
def crearEmpresa(db: Session, empresa: EmpresaCreate) -> EmpresaRead:
    existe = db.exec(select(Empresa).where(Empresa.ruc == empresa.ruc)).first()
    if existe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Empresa con RUC '{empresa.ruc}' ya existe.")
    nuevo = Empresa(**empresa.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
def obtenerEmpresas(db: Session) -> list[EmpresaRead]:
    return db.exec(select(Empresa)).all()
def obtenerEmpresaPorId(db: Session, id: int) -> EmpresaRead:
    empresa = db.get(Empresa, id)
    if not empresa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Empresa con id '{id}' no encontrada.")
    return empresa
def actualizarEmpresa(db: Session, id: int, empresa: EmpresaUpdate) -> EmpresaRead:
    existente = db.get(Empresa, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Empresa con id '{id}' no encontrada.")
    
    datos_por_actualizar = empresa.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar la empresa.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente
def eliminarEmpresa(db: Session, id: int) -> None:
    empresa = db.get(Empresa, id)
    if not empresa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Empresa con id '{id}' no encontrada.")
    db.delete(empresa)
    db.commit()
    return {"detail": f"Empresa con id '{id}' eliminada correctamente."}
