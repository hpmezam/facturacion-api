from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from decimal import Decimal
from app.models.productos import Producto
from datetime import datetime

class PrecioProducto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tipo_precio: str = Field(max_length=50, nullable=False)
    precio: Decimal = Field(nullable=False)
    moneda: str = Field(max_length=10, nullable=False)  
    fecha_inicio: datetime = Field(nullable=False)
    fecha_fin: datetime = Field(nullable=False)
    activo: bool = Field(default=True)
    
    #relaciones claves foraneas
    producto_id: int = Field(foreign_key="producto.id", nullable=False)
    
    # relaciones objetos relacionados 
    producto: Optional['Producto'] = Relationship(back_populates='precioproductos')
