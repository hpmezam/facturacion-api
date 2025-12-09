from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING, List

if TYPE_CHECKING:
    from app.models.persona import Persona

class TipoPersona(SQLModel, table=True):
    __tablename__ = "tipo_persona"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=30, nullable=False, index=True)
    activo: bool = Field(default=True, nullable=False)
    
    # One-to-Many → Persona
    personas: List['Persona'] = Relationship(back_populates='tipo_persona')