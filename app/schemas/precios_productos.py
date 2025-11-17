from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from decimal import Decimal
from app.schemas.productos import ProductoRead
from datetime import datetime

class PrecioProductoBase(SQLModel):
    tipo_precio: str 
    precio: Decimal
    moneda: str 
    fecha_inicio: datetime 
    fecha_fin: datetime 
    activo: bool 
    
    # relaciones claves foraneas
    producto_id: int

class PrecioProductoCreate(PrecioProductoBase):
    pass

class PrecioProductoRead(PrecioProductoBase):
    id: int
    
    #objetos relacionados
    producto: Optional[ProductoRead] = None
    
class PrecioProductoUpdate(SQLModel):
    tipo_precio: Optional[str] = None
    precio: Optional[Decimal] = None
    moneda: Optional[str] = None
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    activo: Optional[bool] = None
    
    #relaciones claves foraneas
    producto_id: Optional[int] = None
    