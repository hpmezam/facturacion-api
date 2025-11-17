from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List, TYPE_CHECKING
from decimal import Decimal
from datetime import datetime

if TYPE_CHECKING:
    from app.models.productos import Producto

class MovimientoInventario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cantidad: Decimal = Field(nullable=False)
    tipo_movimiento: str = Field(max_length=50, nullable=False)  # e.g., 'entrada', 'salida'
    fecha_movimiento: datetime = Field(default=datetime.utcnow, nullable=False)
    descripcion: Optional[str] = Field(max_length=255, nullable=True)
    
    # relaciones claves foraneas
    bodega_id: int = Field(foreign_key="bodega.id", nullable=False)
    producto_id: int = Field(foreign_key="producto.id", nullable=False)
    
    # relaciones objetos relacionados
    producto: Optional['Producto'] = Relationship(back_populates='movimientosinventario')