from sqlmodel import SQLModel, Field
from typing import Optional

class TipoIdentificacion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True, unique=True, max_length=20, nullable=False)
    nombre: str = Field(max_length=50, nullable=False)
    descripcion: Optional[str] = Field(default=None, max_length=100)
    longitud: int = Field(nullable=False)
    activo: bool = Field(default=True)