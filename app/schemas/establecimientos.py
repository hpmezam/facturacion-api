from sqlmodel import SQLModel, Field
from pydantic import field_validator
from typing import Optional
from datetime import date, datetime
class EstablecimientoBase(SQLModel):
    empresa_id: int
    codigo: str
    nombre: str
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    es_matriz: Optional[bool] = False
    activo: Optional[bool] = True
class EstablecimientoCreate(EstablecimientoBase):
    pass
class EstablecimientoRead(EstablecimientoBase):
    pass
class EstablecimientoUpdate(SQLModel):
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    es_matriz: Optional[bool] = None
    activo: Optional[bool] = None
