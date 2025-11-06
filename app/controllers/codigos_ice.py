from sqlmodel import Session, select
from fastapi import HTTPException, status
from app.models.codigos_ice import CodigoICE
from app.schemas.codigos_ice import (
    CodigoICECreate,
    CodigoICERead,
    CodigoICEUpdate
)

def crearCodigoICE(db: Session, codigo_ice: CodigoICECreate) -> CodigoICERead:
    nuevo_codigo_ice = CodigoICE(**codigo_ice.model_dump())
    db.add(nuevo_codigo_ice)
    db.commit()
    db.refresh(nuevo_codigo_ice)
    return nuevo_codigo_ice

def obtenerCodigosICE(db: Session) -> list[CodigoICERead]:
    return db.exec(select(CodigoICE)).all()

def obtenerCodigoICEPorId(db: Session, id: int) -> CodigoICERead:
    codigo_ice = db.get(CodigoICE, id)
    if not codigo_ice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Código ICE con id '{id}' no encontrado.")
    return codigo_ice

def actualizarCodigoICE(db: Session, id: int, codigo_ice: CodigoICEUpdate) -> CodigoICERead:   
    existente = db.get(CodigoICE, id)
    if not existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Código ICE con id '{id}' no encontrado.")
    
    datos_por_actualizar = codigo_ice.model_dump(exclude_unset=True)
    
    no_cambios = all(
        getattr(existente, clave) == valor
        for clave, valor in datos_por_actualizar.items()
    )
    if no_cambios:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No se proporcionaron cambios para actualizar el código ICE.")
    
    for clave, valor in datos_por_actualizar.items():
        setattr(existente, clave, valor)
    
    db.add(existente)
    db.commit()
    db.refresh(existente)
    return existente

def eliminarCodigoICE(db: Session, id: int) -> dict:
    codigo_ice = db.get(CodigoICE, id)
    if not codigo_ice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Código ICE con id '{id}' no encontrado.")
    db.delete(codigo_ice)
    db.commit()
    return {"detail": f"Código ICE con id '{id}' eliminado correctamente."}