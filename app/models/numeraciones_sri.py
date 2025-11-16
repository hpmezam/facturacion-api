from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, datetime ,timezone
class NumeracionSRI(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    establecimiento_id: int = Field(foreign_key="establecimiento.id", nullable=False)
    tipo_comprobante_id: int = Field(foreign_key="tipocomprobante.id", nullable=False)
    numero_autorizacion: str = Field(max_length=50, nullable=False)
    secuencia_inicial: int = Field(default=0, nullable=False)
    secuencia_final: int = Field(nullable=False)
    secuencia_actual: int = Field(default=0, nullable=False)
    fecha_emision: date = Field(nullable=False)
    fecha_caducidad: Optional[date] = Field(default=None)
    activo: bool = Field(default=True)
