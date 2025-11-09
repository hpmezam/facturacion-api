from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Integer
from decimal import Decimal
from typing import Optional, TYPE_CHECKING, List
from app.models.productos import Producto

class CodigoICE(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True, unique=True, max_length=100, nullable=False)
    descripcion: str = Field(max_length=200, nullable=False)
    porcentaje: Decimal = Field(nullable=False)
    activo: bool = Field(default=True)
    
    #relaciones objetos relacionados
    productos: List['Producto'] = Relationship(back_populates='codigoice')