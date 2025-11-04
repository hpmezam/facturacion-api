# schema.py
from sqlmodel import SQLModel, Field
from typing import Optional

class TipoIdentificacionBase(SQLModel):
    codigo: str = Field(index=True, unique=True, max_length=10)
    nombre: str
    descripcion: Optional[str] = None
    longitud: int
    patron_regex: str


class TipoIdentificacion(TipoIdentificacionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TipoIdentificacionCreate(TipoIdentificacionBase):
    pass


class TipoIdentificacionRead(TipoIdentificacionBase):
    id: int


class TipoIdentificacionUpdate(SQLModel):
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    longitud: Optional[int] = None
    patron_regex: Optional[str] = None