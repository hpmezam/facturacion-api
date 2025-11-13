from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.empresas import (
    EmpresaCreate,
    EmpresaRead,
    EmpresaUpdate,
)
from app.controllers.empresas import (
    crearEmpresa,
    obtenerEmpresas,
    obtenerEmpresaPorId,
    actualizarEmpresa,
    eliminarEmpresa,
)
empresas_router = APIRouter(prefix='/empresas', tags=['Empresas'])
@empresas_router.post('/', response_model=EmpresaRead)
def crear_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    return crearEmpresa(db, empresa)

@empresas_router.get('/', response_model=list[EmpresaRead])
def obtener_empresas(db: Session = Depends(get_db)):
    return obtenerEmpresas(db)

@empresas_router.get('/{id}', response_model=EmpresaRead)
def obtener_empresa_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerEmpresaPorId(db, id)

@empresas_router.put('/{id}', response_model=EmpresaRead)
def actualizar_empresa(id: int, empresa: EmpresaUpdate, db: Session = Depends(get_db)):
    return actualizarEmpresa(db, id, empresa)

@empresas_router.delete('/{id}', status_code=204)
def eliminar_empresa(id: int, session: Session = Depends(get_db)):
    """
    Elimina una empresa por su ID.
    Retorna un mensaje de confirmación si se elimina correctamente.
    """
    return eliminarEmpresa(session, id)
