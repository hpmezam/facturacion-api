from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from decimal import Decimal
from app.models.productos import Producto
from datetime import datetime

class CodigoBarras(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True, unique=True, max_length=100, nullable=False)
    principal: bool = Field(default=False)
    
    #relaciones claves foraneas
    producto_id: int = Field(foreign_key="producto.id", nullable=False)
    
    #relaciones objetos relacionados
    producto: List['Producto'] = Relationship(back_populates='codigobarras')