from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.productos import (
    ProductoCreate,
    ProductoRead,
    ProductoUpdate,
)

from app.controllers.productos import (
    crearProducto,
    obtenerProductos,
    obtenerProductoPorId,
    actualizarProducto,
    eliminarProducto
)   

productos_router = APIRouter(prefix='/productos', tags=['Productos'])
@productos_router.post('/', response_model=ProductoRead)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crearProducto(db, producto)

@productos_router.get('/', response_model=list[ProductoRead])
def obtener_productos(db: Session = Depends(get_db)):
    return obtenerProductos(db)

@productos_router.get('/{id}', response_model=ProductoRead)
def obtener_producto_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerProductoPorId(db, id)

@productos_router.put('/{id}', response_model=ProductoRead)
def actualizar_producto(id: int, producto: ProductoUpdate, db: Session = Depends(get_db)):
    return actualizarProducto(db, id, producto)

@productos_router.delete('/{id}', status_code=200)
def eliminar_producto(id: int, session: Session = Depends(get_db)):
    return eliminarProducto(session, id)



