from sqlmodel import SQLModel, Field
from typing import Optional

class TipoPersonaBase(SQLModel):
    nombre: str = Field(max_length=20, nullable=False)
    activo: Optional[bool] = True

class TipoPersonaCreate(TipoPersonaBase):
    pass

class TipoPersonaRead(TipoPersonaBase):
    id: int

class TipoPersonaUpdate(SQLModel):
    nombre: Optional[str] = None
    activo: Optional[bool] = None