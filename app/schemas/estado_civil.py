from sqlmodel import SQLModel, Field
from typing import Optional

class EstadoCivilBase(SQLModel):
    nombre: str = Field(max_length=20, nullable=False)
    activo: Optional[bool] = True

class EstadoCivilCreate(EstadoCivilBase):
    pass

class EstadoCivilRead(EstadoCivilBase):
    id: int

class EstadoCivilUpdate(SQLModel):
    nombre: Optional[str] = None
    activo: Optional[bool] = None
    