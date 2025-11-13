from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date, datetime ,timezone
from enum import Enum
class TipoCertificado(str, Enum):
    FIRMA = "FIRMA"
    SELLO = "SELLO"
    TOKEN = "TOKEN"
    SOFTWARE = "SOFTWARE"
class CertificadoDigital(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    empresa_id: int = Field(foreign_key="empresa.id", nullable=False)
    tipo_certificado: TipoCertificado = Field(nullable=False)
    archivo_ruta: Optional[str] = Field(default=None, max_length=255)
    fecha_emision: Optional[date] = Field(default=None)
    fecha_expiracion: Optional[date] = Field(default=None)
    contrasena: Optional[str] = Field(default=None, max_length=100)
    activo: bool = Field(default=True)
    fecha_creacion : Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))