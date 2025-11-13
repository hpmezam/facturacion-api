from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, datetime ,timezone
class Establecimiento(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    empresa_id: int = Field(foreign_key="empresa.id", nullable=False)
    codigo: str = Field(index=True, unique=True, max_length=20, nullable=False)
    nombre: str = Field(max_length=100, nullable=False)
    direccion: Optional[str] = Field(default=None, max_length=255)
    telefono: Optional[str] = Field(default=None, max_length=20)
    email: Optional[str] = Field(default=None, max_length=100)
    es_matriz: bool = Field(default=False)
    activo: bool = Field(default=True)