from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.categorias_producto import (
    CategoriaProductoCreate,
    CategoriaProductoRead,
    CategoriaProductoUpdate,
)
from app.controllers.categorias_producto import (
    crearCategoriaProducto,
    obtenerCategoriaProductoPorId,
    obtenerCategoriasProducto,
    actualizarCategoriaProducto,
    eliminarCategoriaProducto
    
)

categorias_producto_router = APIRouter(prefix='/categorias_producto', tags=['Categorías de Producto'])

@categorias_producto_router.post('/', response_model=CategoriaProductoRead)
def crear_categoria_producto(categoria_producto: CategoriaProductoCreate, db: Session = Depends(get_db)):
    return crearCategoriaProducto(db, categoria_producto)

@categorias_producto_router.get('/', response_model=list[CategoriaProductoRead])
def obtener_categorias_producto(db: Session = Depends(get_db)):
    return obtenerCategoriasProducto(db)

@categorias_producto_router.get('/{id}', response_model=CategoriaProductoRead)
def obtener_categoria_producto_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerCategoriaProductoPorId(db, id)

@categorias_producto_router.put('/{id}', response_model=CategoriaProductoRead)
def actualizar_categoria_producto(id: int, categoria_producto: CategoriaProductoUpdate, db: Session = Depends(get_db)):
    return actualizarCategoriaProducto(db, id, categoria_producto)

@categorias_producto_router.delete('/{id}', status_code=200)
def eliminar_categoria_producto(id: int, db: Session = Depends(get_db)):
    return eliminarCategoriaProducto(db, id)
