from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Persona(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    numero_identificacion: str = Field(max_length=00, nullable=False)
    nombres: str = Field(max_length=100, index=True, unique=True)
    apellidos: str = Field(max_length=100)
    direccion: Optional[str] = Field(max_length=200)
    telefono: Optional[str] = Field(max_length=10)
    celular: Optional[str] = Field(max_length=10)
    correo_electronico: Optional[str] = Field(max_length=100)
    fecha_nacimiento: Optional[date] = None
    
    
    tipo_identificacion_id: int