from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from app.models.productos import Producto
from decimal import Decimal


class Impuesto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo_sri: str = Field(index=True, max_length=100, nullable=False)
    nombre: str = Field(index=True, max_length=100, nullable=False)
    porcentaje: Decimal = Field(nullable=False)
    descripcion: str = Field(max_length=200, nullable=False)
    activo: bool = Field(default=True)
    
    #relaciones objetos relacionados
    productos: List['Producto'] = Relationship(back_populates='impuesto')