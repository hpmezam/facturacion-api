from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.models.persona import Persona

class TipoIdentificacion(SQLModel, table=True):
    __tablename__ = "tipo_identificacion"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False, index=True)
    descripcion: Optional[str] = Field(default=None, max_length=100)
    longitud: int = Field(nullable=False)
    activo:  bool = Field(default=True, nullable=False)
    
    # One-to-Many → Persona
    personas: List['Persona'] = Relationship(back_populates='tipo_identificacion')