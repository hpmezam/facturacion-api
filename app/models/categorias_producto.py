from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from app.models.productos import Producto

class CategoriaProducto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False, unique=True)
    descripcion: Optional[str] = Field(default=None, max_length=200)
    codigo_sri: str = Field(max_length=20)
    activo: bool = Field(default=True)
    
    #relaciones objetos relaciondos
    productos: List['Producto'] = Relationship(back_populates='categoria')