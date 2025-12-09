from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.tipo_persona import TipoPersona
from app.schemas.tipo_persona import (
    TipoPersonaCreate,
    TipoPersonaRead,
    TipoPersonaUpdate,
)

# Crear un nuevo tipo de persona
def crearTipoPersona(db: Session, tipo_persona: TipoPersonaCreate) -> TipoPersona:
    # Comprobar si ya existe un tipo de persona con el mismo nombre
    existe = db.exec(select(TipoPersona).where(TipoPersona.nombre == tipo_persona.nombre)).first()
    if existe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El tipo de persona con nombre '{tipo_persona.nombre}' ya existe.")
    nuevo = TipoPersona(**tipo_persona.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Obtener todos los tipos de persona
def obtenerTipoPersonas(db: Session) -> list[TipoPersonaRead]:
    return db.exec(select(TipoPersona)).all()

# Obtener un tipo de persona por ID
def obtenerTipoPersonaPorId(db: Session, id: int) -> TipoPersonaRead:
    # Obtener objeto existente
    tipo_persona = db.get(TipoPersona, id)
    if not tipo_persona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tipo de persona con id '{id}' no encontrado.")
    return tipo_persona

# Actualizar un tipo de persona
def actualizarTipoPersona(db: Session, id: int, tipo_persona: TipoPersonaUpdate) -> TipoPersonaRead:
    # 1. Obtener objeto existente
    existente = db.get(TipoPersona, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tipo de persona con id '{id}' no encontrado.")
    
    # 2. Obtener solo los campos que se proporcionaron
    datos_por_actualizar = tipo_persona.model_dump(exclude_unset=True)
    
    # 3. Comprobar si existe un tipo de persona con el mismo nombre
    if 'nombre' in datos_por_actualizar:
        duplicado = db.exec(
            select(TipoPersona)
            .where(TipoPersona.nombre == datos_por_actualizar['nombre'])
            .where(TipoPersona.id != id)
        ).first()
        if duplicado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El tipo de persona con nombre '{datos_por_actualizar['nombre']}' ya existe.")
        
    # 4. Comprobar si los nuevos valores difieren de los actuales
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar el tipo de persona.")
    
    # 5. Actualizar los campos
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente

# Eliminar un tipo de persona
def eliminarTipoPersona(db: Session, id: int) -> dict:
    existente = db.get(TipoPersona, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tipo de persona con id '{id}' no encontrado.")
    nombre = existente.nombre
    db.delete(existente)
    db.commit()
    return {"mensaje": f"Tipo de persona '{nombre}' eliminado correctamente."}