from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, datetime ,timezone
class TipoComprobante(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo_sri: str = Field(max_length=10, nullable=False, unique=True)
    nombre: str = Field(max_length=50, nullable=False)
    descripcion: str = Field(max_length=100, nullable=False)
    activo: bool = Field(default=True)