# crud.py
from sqlmodel import Session, select
from models.schema import (
    TipoIdentificacion,
    TipoIdentificacionCreate,
    TipoIdentificacionUpdate
)

def get_tipos_identificacion(session: Session):
    statement = select(TipoIdentificacion)
    return session.exec(statement).all()

def get_tipo_identificacion(session: Session, tipo_id: int):
    return session.get(TipoIdentificacion, tipo_id)

def create_tipo_identificacion(session: Session, tipo: TipoIdentificacionCreate):
    db_tipo = TipoIdentificacion.from_orm(tipo)
    session.add(db_tipo)
    session.commit()
    session.refresh(db_tipo)
    return db_tipo

def update_tipo_identificacion(session: Session, tipo_id: int, tipo_data: TipoIdentificacionUpdate):
    db_tipo = session.get(TipoIdentificacion, tipo_id)
    if not db_tipo:
        return None
    for key, value in tipo_data.dict(exclude_unset=True).items():
        setattr(db_tipo, key, value)
    session.add(db_tipo)
    session.commit()
    session.refresh(db_tipo)
    return db_tipo

def delete_tipo_identificacion(session: Session, tipo_id: int):
    db_tipo = session.get(TipoIdentificacion, tipo_id)
    if not db_tipo:
        return None
    session.delete(db_tipo)
    session.commit()
    return db_tipo
