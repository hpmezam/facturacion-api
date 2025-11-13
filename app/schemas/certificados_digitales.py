# app/schemas/certificados.py
from sqlmodel import SQLModel
from typing import Optional
from datetime import date, datetime
from enum import Enum

class TipoCertificado(str, Enum):
    FIRMA = "FIRMA"
    SELLO = "SELLO"
    TOKEN = "TOKEN"
    SOFTWARE = "SOFTWARE"


class CertificadoBase(SQLModel):
    tipo_certificado: TipoCertificado
    archivo_ruta: Optional[str] = None
    contrasena: Optional[str] = None
    fecha_emision: Optional[date] = None
    fecha_expiracion: Optional[date] = None
    activo: Optional[bool] = True


class CertificadoCreate(CertificadoBase):
    empresa_id: int   # obligatorio al crear


class CertificadoRead(CertificadoBase):
    pass

class CertificadoUpdate(SQLModel):
    tipo_certificado: Optional[TipoCertificado] = None
    archivo_ruta: Optional[str] = None
    contrasena: Optional[str] = None
    fecha_emision: Optional[date] = None
    fecha_expiracion: Optional[date] = None
    activo: Optional[bool] = None
