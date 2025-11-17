from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.genero import (
    GeneroCreate,
    GeneroRead,
    GeneroUpdate,
)
from app.controllers.genero import (
    crearGenero,
    obtenerGeneros,
    obtenerGeneroPorId,
    actualizarGenero,
    eliminarGenero
)

genero_router = APIRouter(prefix='/genero', tags=['Géneros'])

@genero_router.post('/', response_model=GeneroRead)
def crear_genero(genero: GeneroCreate, db: Session = Depends(get_db)):
    return crearGenero(db, genero)

@genero_router.get('/', response_model=list[GeneroRead])
def obtener_generos(db: Session = Depends(get_db)):
    return obtenerGeneros(db)

@genero_router.get('/{id}', response_model=GeneroRead)
def obtener_genero_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerGeneroPorId(db, id)

@genero_router.put('/{id}', response_model=GeneroRead)
def actualizar_genero(id: int, genero: GeneroUpdate, db: Session = Depends(get_db)):
    return actualizarGenero(db, id, genero)

@genero_router.delete('/{id}', status_code=200)
def eliminar_genero(id: int, session: Session = Depends(get_db)):
    return eliminarGenero(session, id)