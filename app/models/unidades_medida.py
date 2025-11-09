from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from app.models.productos import Producto


class UnidadMedida(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True, unique=True, max_length=100, nullable=False)
    nombre: str = Field(max_length=50, nullable=False)
    simbolo: str = Field(max_length=10, nullable=False)
    activo: bool = Field(default=True)
    
    #relaciones objetos relacionados
    productos: List['Producto'] = Relationship(back_populates='unidadmedida')
    
    