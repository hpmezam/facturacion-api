from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.genero import Genero
from app.schemas.genero import (
    GeneroCreate,
    GeneroRead,
    GeneroUpdate,
)

# Crear un nuevo género
def crearGenero(db: Session, genero: GeneroCreate) -> GeneroRead:
    # Comprobar si ya existe un género con el mismo nombre
    existe = db.exec(select(Genero).where(Genero.nombre == genero.nombre)).first()
    if existe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El género con nombre '{genero.nombre}' ya existe.")
    nuevo = Genero(**genero.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Obtener todos los géneros
def obtenerGeneros(db: Session) -> list[GeneroRead]:
    return db.exec(select(Genero)).all()

# Obtener un género por ID
def obtenerGeneroPorId(db: Session, id: int) -> GeneroRead:
    # 1. Obtener objeto existente
    genero = db.get(Genero, id)
    if not genero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Género con id '{id}' no encontrado.")
    return genero

# Actualizar un género
def actualizarGenero(db: Session, id: int, genero: GeneroUpdate) -> GeneroRead:
    # 1. Obtener objeto existente
    existente = db.get(Genero, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Género con id '{id}' no encontrado.")
    
    # 2. Obtener solo los campos que se proporcionaron
    datos_por_actualizar = genero.model_dump(exclude_unset=True)
    
    # 3. Comprobar si existe un género con el mismo nombre
    if 'nombre' in datos_por_actualizar:
        duplicado = db.exec(
            select(Genero)
            .where(Genero.nombre == datos_por_actualizar['nombre'])
            .where(Genero.id != id)
        ).first()
        if duplicado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El género con nombre '{datos_por_actualizar['nombre']}' ya existe.")
        
    # 4. Comprobar si los nuevos valores difieren de los actuales
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar el género.")

    # 5. Actualizar los campos
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente

# Eliminar un género
def eliminarGenero(db: Session, id: int) -> dict:
    genero = db.get(Genero, id)
    if not genero:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Género con id '{id}' no encontrado.")
    nombre = genero.nombre
    db.delete(genero)
    db.commit()
    return {"mensaje": f"Género '{nombre}' eliminado correctamente."}