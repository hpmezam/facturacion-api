from sqlmodel import SQLModel, Field
from pydantic import field_validator
from typing import Optional
from datetime import date, datetime
class NumeracionSRIBase(SQLModel):
    establecimiento_id: int
    tipo_comprobante_id: int
    numero_autorizacion: str
    secuencia_inicial: int = 0
    secuencia_final: int
    secuencia_actual: int = 0
    fecha_emision: date
    fecha_caducidad: Optional[date] = None
    activo: bool = True
class NumeracionSRICreate(NumeracionSRIBase):
    pass
class NumeracionSRIRead(NumeracionSRIBase):
    pass

class NumeracionSRIUpdate(SQLModel):
    establecimiento_id: Optional[int] = None
    tipo_comprobante_id: Optional[int] = None
    numero_autorizacion: Optional[str] = None
    secuencia_inicial: Optional[int] = None
    secuencia_final: Optional[int] = None
    secuencia_actual: Optional[int] = None
    fecha_emision: Optional[date] = None
    fecha_caducidad: Optional[date] = None
    activo: Optional[bool] = None