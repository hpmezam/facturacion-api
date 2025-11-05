# schema.py
from sqlmodel import SQLModel, Field
from typing import Optional

class TipoIdentificacionBase(SQLModel):
    codigo: str
    nombre: str
    descripcion: Optional[str] = None
    longitud: int
    patron_regex: str
    activo: bool = True

class TipoIdentificacionCreate(TipoIdentificacionBase):
    pass

class TipoIdentificacionRead(TipoIdentificacionBase):
    pass

class TipoIdentificacionUpdate(SQLModel):
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    longitud: Optional[int] = None
    patron_regex: Optional[str] = None
    activo: Optional[bool] = None