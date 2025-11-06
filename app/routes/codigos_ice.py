from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.config.session import get_db
from app.schemas.codigos_ice import (
    CodigoICECreate,
    CodigoICERead,
    CodigoICEUpdate,
)

from app.controllers.codigos_ice import (
    crearCodigoICE,
    obtenerCodigosICE,
    obtenerCodigoICEPorId,
    actualizarCodigoICE,
    eliminarCodigoICE
)

codigos_ice_router = APIRouter(prefix='/codigos_ice', tags=['Códigos ICE'])
@codigos_ice_router.post('/', response_model=CodigoICERead)

def crear_codigo_ice(codigo_ice: CodigoICECreate, db: Session = Depends(get_db)):
    return crearCodigoICE(db, codigo_ice)

@codigos_ice_router.get('/', response_model=list[CodigoICERead])
def obtener_codigos_ice(db: Session = Depends(get_db)):
    return obtenerCodigosICE(db)

@codigos_ice_router.get('/{id}', response_model=CodigoICERead)
def obtener_codigo_ice_por_id(id: int, db: Session = Depends(get_db)):
    return obtenerCodigoICEPorId(db, id)

@codigos_ice_router.put('/{id}', response_model=CodigoICERead)
def actualizar_codigo_ice(id: int, codigo_ice: CodigoICEUpdate, db: Session = Depends(get_db)):
    return actualizarCodigoICE(db, id, codigo_ice)

@codigos_ice_router.delete('/{id}', status_code=200)
def eliminar_codigo_ice(id: int, session: Session = Depends(get_db)):
    return eliminarCodigoICE(session, id)

 