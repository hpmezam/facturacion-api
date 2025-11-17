from sqlmodel import Session, select
from fastapi import HTTPException, status
from typing import List, Optional
from decimal import Decimal
from app.models.productos import Producto
from app.models.categorias_producto import CategoriaProducto
from app.models.unidades_medida import UnidadMedida
from app.models.impuestos import Impuesto
from app.models.codigos_ice import CodigoICE

from app.schemas.productos import (
    ProductoCreate,
    ProductoRead,
    ProductoUpdate
)

"""
metodo para validar la existencia de relaciones foraneas
"""
def validar_relacion(db: Session, modelo: type, id_valor: int | None, nombre_entidad: str):
    if id_valor:
        entidad = db.get(modelo, id_valor)
        if not entidad:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"{nombre_entidad} con ID {id_valor} no encontrada"
            )
        return entidad
    return None

"""
metodo crearProducto, me permite crear un nuevo producto en la base de datos
"""
def crearProducto(db: Session, producto: ProductoCreate) -> ProductoRead:
    producto_exieste = db.exec(
        select(Producto).where(Producto.codigo_principal == producto.codigo_principal)
    ).first()
    if producto_exieste:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El código principal '{producto.codigo_principal}' ya está en uso por otro producto."
        )
    # validaciom de claves foraneas
    validar_relacion(db, CategoriaProducto, producto.categoria_id, "Categoría de producto")
    validar_relacion(db, UnidadMedida, producto.unidad_medida_id, "Unidad de medida")
    validar_relacion(db, Impuesto, producto.impuesto_id, "Impuesto")
    validar_relacion(db, CodigoICE, producto.codigo_ice_id, "Código ICE")
    
    nuevo_producto = Producto(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

"""

"""
def obtenerProductos(db: Session) -> list[ProductoRead]:
    return db.exec(select(Producto)).all()

def obtenerProductoPorId(db: Session, id: int) -> ProductoRead:
    producto = db.get(Producto, id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id '{id}' no encontrado.")
    return producto

def actualizarProducto(db: Session, id_producto: int, producto_update: ProductoUpdate) -> ProductoRead:   
    producto_existente  = db.get(Producto, id_producto)
    if not producto_existente :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Producto con id '{id_producto}' no encontrado.")
    
    if producto_update.codigo_principal:
        producto_existente  = db.exec(
            select(Producto).where(
                Producto.codigo_principal == producto_update.codigo_principal,
                Producto.id != id_producto
            )
        ).first()
        
        if producto_existente :
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe otro producto con el código principal: {producto_update.codigo_principal}"
            )
    
    # Validar relaciones (si se proporcionaron IDs)
    if producto_update.categoria_id is not None:
        categoria = db.get(CategoriaProducto, producto_update.categoria_id)
        if not categoria and producto_update.categoria_id != 0:  # 0 podría ser para quitar relación
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Categoría con ID {producto_update.categoria_id} no encontrada"
            )
    
    if producto_update.unidad_medida_id is not None:
        unidad_medida = db.get(UnidadMedida, producto_update.unidad_medida_id)
        if not unidad_medida:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Unidad de medida con ID {producto_update.unidad_medida_id} no encontrada"
            )
   
   
    datos_por_actualizar = producto_update.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(producto_existente , clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se proporcionaron cambios para actualizar el producto."\
        )
    
    for clave, valor in datos_por_actualizar.items():
        setattr(producto_existente , clave, valor)
    
    db.add(producto_existente)
    db.commit()
    db.refresh(producto_existente)
    return producto_existente 

def eliminarProducto(db: Session, id: int) -> dict:
    producto = db.get(Producto, id)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Producto con id '{id}' no encontrado.")
    db.delete(producto)
    db.commit()
    return {"detail": f"Producto con id '{id}' eliminado correctamente."}

