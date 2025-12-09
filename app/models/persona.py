from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.models.tipo_identificacion import TipoIdentificacion
    from app.models.tipo_persona import TipoPersona
    from app.models.estado_civil import EstadoCivil

class Persona(SQLModel, table=True):
    __tablename__ = "persona"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    numero_identificacion: str = Field(max_length=100, nullable=False)
    nombres: str = Field(max_length=100, index=True)
    apellidos: str = Field(max_length=100)
    direccion: Optional[str] = Field(max_length=200)
    telefono: Optional[str] = Field(max_length=10)
    correo_electronico: Optional[str] = Field(max_length=100)
    es_contribuyente: bool
    activo: bool
    
    # Claves foráneas
    tipo_persona_id: Optional[int] = Field(default=None, foreign_key="tipo_persona.id")
    tipo_identificacion_id: Optional[int] = Field(default=None, foreign_key="tipo_identificacion.id")
    estado_civil_id: Optional[int] = Field(default=None, foreign_key="estado_civil.id")
    
    # Relaciones
    tipo_persona: Optional['TipoPersona'] = Relationship(back_populates='personas')
    tipo_identificacion: Optional['TipoIdentificacion'] = Relationship(back_populates='personas')
    estado_civil: Optional['EstadoCivil'] = Relationship(back_populates='personas')