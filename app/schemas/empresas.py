from sqlmodel import SQLModel, Field
from pydantic import field_validator
from typing import Optional
from datetime import date, datetime
from app.utils.validadores import validar_ruc_ecuador

class EmpresaBase(SQLModel):
    ruc: str = Field(max_length=13, min_length=13)
    # @field_validator("ruc")
    # def validar_ruc(cls, ruc):
    #     return validar_ruc_ecuador(ruc)
    razon_social: str
    nombre: str
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    logo_url: Optional[str] = None
    obligado_contabilidad: Optional[bool] = False
    agente_retencion: Optional[bool] = False
    contribuyente_especial: Optional[bool] = False
    resolucion_contribuyente: Optional[str] = None
    lleva_contabilidad: Optional[bool] = False
    fecha_inicio_actividades: Optional[date] = None

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaRead(EmpresaBase):
   pass
class EmpresaUpdate(SQLModel):
    ruc: Optional[str] = None
    razon_social: Optional[str] = None
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    logo_url: Optional[str] = None
    obligado_contabilidad: Optional[bool] = None
    agente_retencion: Optional[bool] = None
    contribuyente_especial: Optional[bool] = None
    resolucion_contribuyente: Optional[str] = None
    lleva_contabilidad: Optional[bool] = None
    fecha_inicio_actividades: Optional[date] = None
    estado: Optional[bool] = None
