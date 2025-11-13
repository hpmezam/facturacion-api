from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, datetime ,timezone

class Empresa(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ruc: str = Field(index=True, unique=True, max_length=13, nullable=False)
    razon_social: str = Field(max_length=100, nullable=False)
    nombre: str = Field(max_length=100, nullable=False)
    direccion: Optional[str] = Field(default=None, description="Dirección completa")
    telefono: Optional[str] = Field(default=None, max_length=20)
    email: Optional[str] = Field(default=None, max_length=100)
    website: Optional[str] = Field(default=None, max_length=100)
    logo_url: Optional[str] = Field(default=None, max_length=255)

    obligado_contabilidad: Optional[bool] = Field(default=False)
    agente_retencion: Optional[bool] = Field(default=False)
    contribuyente_especial: Optional[bool] = Field(default=False)
    resolucion_contribuyente: Optional[str] = Field(default=None, max_length=100)
    lleva_contabilidad: Optional[bool] = Field(default=False)

    fecha_inicio_actividades: Optional[date] = Field(default=None)
    fecha_creacion: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    fecha_actualizacion: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    estado: Optional[bool] = Field(default=True)