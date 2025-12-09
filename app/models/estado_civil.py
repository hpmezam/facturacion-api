from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.models.persona import Persona

class EstadoCivil(SQLModel, table=True):
    __tablename__ = "estado_civil"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=30, nullable=False)
    activo: bool
    
    # Relaciones
    personas: List['Persona'] = Relationship(back_populates='estado_civil')