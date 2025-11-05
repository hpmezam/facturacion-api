from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.tipos_identificacion import TipoIdentificacion
from app.schemas.tipos_identificacion import (
    TipoIdentificacionCreate,
    TipoIdentificacionRead,
    TipoIdentificacionUpdate,
)

# Crear un nuevo tipo de identificación
def crearTipoIdentificacion(db: Session, tipo_identificacion: TipoIdentificacionCreate) -> TipoIdentificacionRead:
    # Comprobar si ya existe un tipo de identificación con el mismo nombre
    existe = db.exec(select(TipoIdentificacion).where(TipoIdentificacion.nombre == tipo_identificacion.nombre)).first()
    if existe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El tipo de identificación con nombre '{tipo_identificacion.nombre}' ya existe.")
    nuevo = TipoIdentificacion(**tipo_identificacion.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Obtener todos los tipos de identificación
def obtenerTipoIdentificacions(db: Session) -> list[TipoIdentificacionRead]:
    return db.exec(select(TipoIdentificacion)).all()

# Obtener un tipo de identificación por ID
def obtenerTipoIdentificacionPorId(db: Session, id: int) -> TipoIdentificacionRead:
    # 1. Obtener objeto existente
    tipo_identificacion = db.get(TipoIdentificacion, id)
    if not tipo_identificacion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tipo de identificación con id '{id}' no encontrado.")
    return tipo_identificacion

# Actualizar un tipo de identificación
def actualizarTipoIdentificacion(db: Session, id: int, tipo_identificacion: TipoIdentificacionUpdate) -> TipoIdentificacionRead:
    # 1. Obtener objeto existente
    existente = db.get(TipoIdentificacion, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tipo de identificación con id '{id}' no encontrado.")
    
    # 2. Obtener solo los campos que se proporcionaron
    datos_por_actualizar = tipo_identificacion.model_dump(exclude_unset=True)
    
    # 3. Comprobar si existe un tipo de identificación con el mismo nombre
    if 'nombre' in datos_por_actualizar:
        duplicado = db.exec(
            select(TipoIdentificacion)
            .where(TipoIdentificacion.nombre == datos_por_actualizar['nombre'])
            .where(TipoIdentificacion.id != id)
        ).first()
        if duplicado:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El tipo de identificación con nombre '{datos_por_actualizar['nombre']}' ya existe.")
        
    # 4. Comprobar si los nuevos valores difieren de los actuales
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar el tipo de identificación.")
    
    # 5. Aplicar actualizaciones
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
        
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente

# Eliminar un tipo de identificación
def eliminarTipoIdentificacion(db: Session, id: int) -> dict:
    tipo_identificacion = db.get(TipoIdentificacion, id)
    if not tipo_identificacion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Tipo de identificación con id '{id}' no encontrado.")
    
    nombre = tipo_identificacion.nombre
    db.delete(tipo_identificacion)
    db.commit()
    return {"mensaje": f"Tipo de identificación '{nombre}' eliminado correctamente."}