from sqlmodel import Session, select
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from decimal import Decimal
from app.models.precios_productos import PrecioProducto
from app.models.productos import Producto
from app.schemas.precios_productos import (
    PrecioProductoCreate,
    PrecioProductoRead,
    PrecioProductoUpdate
    
)

def crearPrecioProducto(db: Session, precio_producto: PrecioProductoCreate) -> PrecioProducto:
    producto_existente = db.get(Producto, precio_producto.producto_id)
    if not producto_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con ID {precio_producto.producto_id} no encontrado"
        )
    nuevo_precio_producto = PrecioProducto(**precio_producto.model_dump())
    db.add(nuevo_precio_producto)
    db.commit()
    db.refresh(nuevo_precio_producto)
    return nuevo_precio_producto

def obtenerPreciosProductos(db: Session) -> list[PrecioProducto]:
    return db.exec(select(PrecioProducto)).all()

def obtenerPrecioProductoPorId(db: Session, precio_producto_id: int) -> PrecioProductoRead:
    precio_producto = db.get(PrecioProducto, precio_producto_id)
    if not precio_producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"PrecioProducto con ID {precio_producto_id} no encontrado"
        )
    return precio_producto

def actualizarPrecioProducto(db: Session, ide_precio_producto: int, precio_prod_update: PrecioProductoUpdate) -> PrecioProductoRead:
    precio_producto_existente = db.get(PrecioProducto, ide_precio_producto)
    if not precio_producto_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"PrecioProducto con ID {ide_precio_producto} no encontrado"
        )
    
    if precio_prod_update.producto_id is not None:
        producto=db.get(Producto, precio_prod_update.producto_id)
        if not producto and precio_prod_update.producto_id !=0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con ID {precio_prod_update.producto_id} no encontrado"
            )
    
    datos_poe_actualizar = precio_prod_update.model_dump(exclude_unset=True)
    no_cambios = all(
        getattr(precio_producto_existente, clave) == valor
        for clave, valor in datos_poe_actualizar.items()
    )
    
    if no_cambios:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se proporcionaron cambios para actualizar el precio del producto."
        )
    
    for clave, valor in datos_poe_actualizar.items():
        setattr(precio_producto_existente, clave, valor)
    
    db.add(precio_producto_existente)
    db.commit()
    db.refresh(precio_producto_existente)
    return precio_producto_existente


def eliminarPrecioProducto(db: Session, id: int) -> dict:
    precio_producto = db.get(PrecioProducto, id)
    if not precio_producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"PrecioProducto con ID {id} no encontrado"
        )
    db.delete(precio_producto)
    db.commit()
    return {"detalle": f"PrecioProducto con ID {id} eliminado exitosamente"}
    