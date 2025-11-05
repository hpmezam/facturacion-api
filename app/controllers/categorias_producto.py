from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.categorias_producto import CategoriaProducto
from app.schemas.categorias_producto import (
    CategoriaProductoCreate,
    CategoriaProductoRead,
    CategoriaProductoUpdate,
)

# Crear una nueva categoría de producto
def crearCategoriaProducto(db: Session, categoria_producto: CategoriaProductoCreate) -> CategoriaProductoRead:
    nuevo = CategoriaProducto(**categoria_producto.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtenerCategoriasProducto(db: Session) -> list[CategoriaProductoRead]:
    return db.exec(select(CategoriaProducto)).all()

def obtenerCategoriaProductoPorId(db: Session, id: int) -> CategoriaProductoRead:
    categoria_producto = db.get(CategoriaProducto, id)
    if not categoria_producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoría de producto con id '{id}' no encontrada.")
    return categoria_producto

def actualizarCategoriaProducto(db: Session, id: int, categoria_producto: CategoriaProductoUpdate) -> CategoriaProductoRead:
    existente = db.get(CategoriaProducto, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoría de producto con id '{id}' no encontrada.")
    
    datos_por_actualizar = categoria_producto.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar la categoría de producto.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente

def eliminarCategoriaProducto(db: Session, id: int) -> None:
    categoria_producto = db.get(CategoriaProducto, id)
    if not categoria_producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoría de producto con id '{id}' no encontrada.")
    db.delete(categoria_producto)
    db.commit()
    return {"detail": f"Categoría de producto con id '{id}' eliminada correctamente."}