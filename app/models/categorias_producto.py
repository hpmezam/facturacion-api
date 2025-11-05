from sqlmodel import SQLModel, Field
from typing import Optional

class CategoriaProducto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    descripcion: Optional[str] = Field(default=None, max_length=200)
    codigo_sri: str = Field(max_length=20)
    activo: bool = Field(default=True)