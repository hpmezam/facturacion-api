from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.certificados_digitales import CertificadoDigital
from app.models.empresas import Empresa
from app.schemas.certificados_digitales import (
    CertificadoCreate,
    CertificadoRead,
    CertificadoUpdate
    )
# Crear un nuevo certificado digital
def crearCertificadoDigital(db: Session, certificado_digital: CertificadoCreate) -> CertificadoRead:
    empresa = db.get(Empresa, certificado_digital.empresa_id)
    if not empresa:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La empresa con ID {certificado_digital.empresa_id} no existe."
        )
    nuevo = CertificadoDigital(**certificado_digital.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo
def obtenerCertificadosDigitales(db: Session) -> list[CertificadoRead]:
    return db.exec(select(CertificadoDigital)).all()
def obtenerCertificadoDigitalPorId(db: Session, id: int) -> CertificadoRead:
    certificado_digital = db.get(CertificadoDigital, id)
    if not certificado_digital:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Certificado digital con id '{id}' no encontrado.")
    return certificado_digital
def actualizarCertificadoDigital(db: Session, id: int, certificado_digital: CertificadoUpdate) -> CertificadoRead:
    existente = db.get(CertificadoDigital, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Certificado digital con id '{id}' no encontrado.")
    
    datos_por_actualizar = certificado_digital.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar el certificado digital.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente
def eliminarCertificadoDigital(db: Session, id: int) -> None:
    certificado_digital = db.get(CertificadoDigital, id)
    if not certificado_digital:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Certificado digital con id '{id}' no encontrado.")
    db.delete(certificado_digital)
    db.commit()
    return {"detail": f"Certificado digital con id '{id}' eliminado correctamente."}