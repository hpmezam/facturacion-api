from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime
from app.schemas.categorias_producto import CategoriaProductoRead
from app.schemas.unidades_medida import UnidadMedidaRead
from app.schemas.impuestos import ImpuestoRead
from app.schemas.codigos_ice import CodigoICERead
from decimal import Decimal


class ProductoBase(SQLModel):
    codigo_principal: str 
    codigo_auxiliar: str 
    nombre: str
    descripcion: Optional[str] = None
    tipo_producto: Optional[str] = None
    iva_porcetaje: Decimal
    ice_porcetaje: Optional[Decimal] = None
    irbpnr_porcetaje: Optional[Decimal] = None
    stock_minimo: Optional[Decimal] = None
    peso: Optional[Decimal] = None
    voumen: Optional[Decimal] = None
    imagen_url: Optional[str] = None
    activo: bool 
    fecha_creacion: datetime 
    fecha_actualizacion: datetime 
    
    #relaciones claves foraneas
    categoria_id: Optional[int] = None
    unidad_medida_id: Optional[int] = None
    impuesto_id: Optional[int] = None
    codigo_ice_id: Optional[int] = None
    
    
class ProductoCreate(ProductoBase):
    pass
    
class ProductoRead(ProductoBase):
    id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    # OBJETOS RELACIONADOS COMPLETOS (no solo IDs)
    categoria: Optional[CategoriaProductoRead] = None
    unidad_medida: Optional[UnidadMedidaRead] = None
    impuesto: Optional[ImpuestoRead] = None
    codigo_ice: Optional[CodigoICERead] = None
    pass

class ProductoUpdate(SQLModel):
    codigo_principal: str 
    codigo_auxiliar: str 
    nombre: str
    descripcion: Optional[str] = None
    tipo_producto: Optional[str] = None
    iva_porcetaje: Decimal
    ice_porcetaje: Optional[Decimal] = None
    irbpnr_porcetaje: Optional[Decimal] = None
    stock_minimo: Optional[Decimal] = None
    peso: Optional[Decimal] = None
    voumen: Optional[Decimal] = None
    imagen_url: Optional[str] = None
    activo: bool 
    fecha_creacion: datetime 
    fecha_actualizacion: datetime
    
    #relaciones claves foraneas
    categoria_id: Optional[int] = None
    unidad_medida_id: Optional[int] = None
    impuesto_id: Optional[int] = None
    codigo_ice_id: Optional[int] = None


