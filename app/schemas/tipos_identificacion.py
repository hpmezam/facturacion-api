# schema.py
from sqlmodel import SQLModel, Field
from typing import Optional

class TipoIdentificacionBase(SQLModel):
    nombre: str = Field(max_length=50, nullable=False)
    descripcion: Optional[str] = Field(default=None, max_length=100)
    longitud: int = Field(nullable=False)
    activo: Optional[bool] = True

class TipoIdentificacionCreate(TipoIdentificacionBase):
    pass

class TipoIdentificacionRead(TipoIdentificacionBase):
    id: int

class TipoIdentificacionUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    longitud: Optional[int] = None
    activo: Optional[bool] = None