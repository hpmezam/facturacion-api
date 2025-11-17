from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db

from app.schemas.precios_productos import (
    PrecioProductoCreate,
    PrecioProductoRead,
    PrecioProductoUpdate
)

from app.controllers.precios_productos import (
    crearPrecioProducto,
    obtenerPreciosProductos,
    obtenerPrecioProductoPorId,
    actualizarPrecioProducto,
    eliminarPrecioProducto
)

precios_productos_router = APIRouter(prefix='/precios_productos', tags=['Precios de Productos'])
@precios_productos_router.post('/', response_model=PrecioProductoRead)
def crear_precio_producto(precio_producto: PrecioProductoCreate, db: Session = Depends(get_db)):
    return crearPrecioProducto(db, precio_producto) 

@precios_productos_router.get('/', response_model=list[PrecioProductoRead])
def obtener_precios_productos(db: Session = Depends(get_db)):
    return obtenerPreciosProductos(db)

@precios_productos_router.get('/{id}', response_model=PrecioProductoRead)
def obtener_precio_producto_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerPrecioProductoPorId(db, id)

@precios_productos_router.put('/{id}', response_model=PrecioProductoRead)
def actualizar_precio_producto(id: int, precio_producto: PrecioProductoUpdate, db: Session = Depends(get_db)):
    return actualizarPrecioProducto(db, id, precio_producto)

@precios_productos_router.delete('/{id}', status_code=200)
def eliminar_precio_producto(id: int, session: Session = Depends(get_db)):
    return eliminarPrecioProducto(session, id)

