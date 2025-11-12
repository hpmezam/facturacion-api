# schema.py
from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import BaseModel, constr, field_validator
from pydantic import validator
class TipoIdentificacionBase(SQLModel):
    codigo: str = Field(index=True, unique=True, max_length=20, nullable=False)
    nombre: str = Field(max_length=50, nullable=False)
    descripcion: Optional[str] = Field(default=None, max_length=100)
    longitud: int = Field(nullable=False)
    activo: bool = Field(default=True)

class TipoIdentificacionCreate(TipoIdentificacionBase):
    pass

class TipoIdentificacionRead(TipoIdentificacionBase):
    pass

class TipoIdentificacionUpdate(SQLModel):
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    longitud: Optional[int] = None
    activo: Optional[bool] = None