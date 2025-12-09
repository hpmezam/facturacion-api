from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.estado_civil import EstadoCivil
from app.schemas.estado_civil import (
    EstadoCivilCreate,
    EstadoCivilRead,
    EstadoCivilUpdate,
)

# Crear un nuevo estado civil
def crearEstadoCivil(db: Session, estado_civil: EstadoCivilCreate) -> EstadoCivil:
    # Comprobar si ya existe un estado civil con el mismo nombre
    existe = db.exec(select(EstadoCivil).where(EstadoCivil.nombre == estado_civil.nombre)).first()
    if existe:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"El estado civil con nombre '{estado_civil.nombre}' ya existe.")
    nuevo = EstadoCivil(**estado_civil.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

# Obtener todos los estados civiles
def obtenerEstadosCiviles(db: Session) -> list[EstadoCivilRead]:
    return db.exec(select(EstadoCivil)).all()


# Obtener estado civil por ID
def obtenerEstadoCivilPorId(db: Session, id: int) -> EstadoCivilRead:
    estado = db.get(EstadoCivil, id)
    if not estado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Estado civil con id '{id}' no encontrado."
        )
    return estado


# Actualizar un estado civil
def actualizarEstadoCivil(db: Session, id: int, estado: EstadoCivilUpdate) -> EstadoCivilRead:
    existente = db.get(EstadoCivil, id)
    if not existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Estado civil con id '{id}' no encontrado."
        )

    datos_por_actualizar = estado.model_dump(exclude_unset=True)

    # Validar duplicado en nombre
    if "nombre" in datos_por_actualizar:
        duplicado = db.exec(
            select(EstadoCivil)
            .where(EstadoCivil.nombre == datos_por_actualizar["nombre"])
            .where(EstadoCivil.id != id)
        ).first()
        if duplicado:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El estado civil '{datos_por_actualizar['nombre']}' ya existe."
            )

    # Detectar si no hay cambios
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No se proporcionaron cambios para actualizar el estado civil."
        )

    # Aplicar cambios
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)

    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente


# Eliminar un estado civil
def eliminarEstadoCivil(db: Session, id: int) -> dict:
    estado = db.get(EstadoCivil, id)
    if not estado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Estado civil con id '{id}' no encontrado."
        )
    
    nombre = estado.nombre
    db.delete(estado)
    db.commit()

    return {"mensaje": f"Estado civil '{nombre}' eliminado correctamente."}