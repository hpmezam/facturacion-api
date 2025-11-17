from sqlmodel import SQLModel, Field
from typing import Optional

class GeneroBase(SQLModel):
    nombre: str = Field(max_length=20, nullable=False)
    activo: Optional[bool] = True

class GeneroCreate(GeneroBase):
    pass

class GeneroRead(GeneroBase):
    id: int

class GeneroUpdate(SQLModel):
    nombre: Optional[str] = None
    activo: Optional[bool] = None