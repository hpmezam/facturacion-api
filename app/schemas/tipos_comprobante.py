from sqlmodel import SQLModel, Field
from pydantic import field_validator
from typing import Optional
from datetime import date, datetime
class TipoComprobanteBase(SQLModel):
    codigo_sri: str
    nombre: str
    descripcion: str
    activo: bool = True
class TipoComprobanteCreate(TipoComprobanteBase):
    pass
class TipoComprobanteRead(TipoComprobanteBase):
    pass
class TipoComprobanteUpdate(SQLModel):
    codigo_sri: Optional[str] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    activo: Optional[bool] = None
