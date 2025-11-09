from sqlmodel import SQLModel, Field
from typing import Optional
from decimal import Decimal

class Impuesto(SQLModel):
    codigo_sri: str
    nombre: str
    porcentaje: Decimal
    descripcion: str
    activo: bool = True

class ImpuestoCreate(Impuesto):
    pass

class ImpuestoRead(Impuesto):
    id: int
    pass

class ImpuestoUpdate(SQLModel):
    codigo_sri: Optional[str] = None
    nombre: Optional[str] = None
    porcentaje: Optional[Decimal] = None
    descripcion: Optional[str] = None
    activo: Optional[bool] = None

 
    