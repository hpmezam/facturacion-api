from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.certificados_digitales import (
    CertificadoCreate,
    CertificadoRead,
    CertificadoUpdate,
)
from app.controllers.certificados_digitales import (
    crearCertificadoDigital as crearCertificado,
    obtenerCertificadosDigitales as obtenerCertificados,
    obtenerCertificadoDigitalPorId as obtenerCertificadoPorId,
    actualizarCertificadoDigital as actualizarCertificado,
    eliminarCertificadoDigital as eliminarCertificado,
)
certificados_router = APIRouter(prefix='/certificados_digitales', tags=['Certificados Digitales'])
@certificados_router.post('/', response_model=CertificadoRead)
def crear_certificado(certificado: CertificadoCreate, db: Session = Depends(get_db)):
    return crearCertificado(db, certificado)
@certificados_router.get('/', response_model=list[CertificadoRead])
def obtener_certificados(db: Session = Depends(get_db)):
    return obtenerCertificados(db)
@certificados_router.get('/{id}', response_model=CertificadoRead)
def obtener_certificado_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerCertificadoPorId(db, id)
@certificados_router.put('/{id}', response_model=CertificadoRead)
def actualizar_certificado(id: int, certificado: CertificadoUpdate, db: Session = Depends(get_db)):
    return actualizarCertificado(db, id, certificado)
@certificados_router.delete('/{id}', status_code=204)
def eliminar_certificado(id: int, session: Session = Depends(get_db)):
    """
    Elimina un certificado digital por su ID.
    Retorna un mensaje de confirmación si se elimina correctamente.
    """
    return eliminarCertificado(session, id)