from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from decimal import Decimal
from app.models.productos import Producto
from datetime import datetime

class MovimientoInventario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primaary_key=True)
    
    
    bodega_id: int = Field(foreign_key="bodega.id", nullable=False)
    producto_id: int = Field(foreign_key="producto.id", nullable=False)
    
    