from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING, List
from sqlalchemy import Column, Integer
from datetime import datetime
from decimal import Decimal

from app.models.categorias_producto import CategoriaProducto
from app.models.unidades_medida import UnidadMedida
from app.models.impuestos import Impuesto
from app.models.codigos_ice import CodigoICE
from app.models.precios_productos import PrecioProducto
from app.models.codigos_barras import CodigoBarras


class Producto(SQLModel, table=True):
    #campos de la tabla
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo_principal: str = Field(index=True, unique=True, max_length=20, nullable=False)
    codigo_auxiliar: str = Field(index=True, max_length=20, nullable=False)
    nombre: str = Field(index=True, max_length=100, nullable=False)
    descripcion: Optional[str] = Field(default=None, max_length=200)
    tipo_producto: Optional[str] = Field(default=None, max_length=200)
    iva_porcetaje: Decimal = Field(default=0.0, nullable=False)
    ice_porcetaje: Optional[Decimal] = Field(default=0.0)
    irbpnr_porcetaje: Optional[Decimal] = Field(default=0.0)
    stock_minimo: Optional[Decimal] = Field(default=0.0)
    peso: Optional[Decimal] = Field(default=0.0)
    voumen: Optional[Decimal] = Field(default=0.0)
    imagen_url: Optional[str] = Field(default=None, max_length=200)
    activo: bool = Field(default=True)
    fecha_creacion: datetime = Field(default_factory=datetime.now, nullable=False)
    fecha_actualizacion: datetime = Field(nullable=False)
    
    #relaciones claves foraneas
    categoria_id: Optional[int] = Field(default=None, foreign_key="categoriaproducto.id")
    unidad_medida_id: Optional[int] = Field(default=None, foreign_key="unidadmedida.id")
    impuesto_id: Optional[int] = Field(default=None, foreign_key="impuesto.id")
    codigo_ice_id: Optional[int] = Field(default=None, foreign_key="codigoice.id")
    
    #relaciones objetos relacionados
    categoria: Optional['CategoriaProducto'] = Relationship(back_populates='productos')
    unidadmedida: Optional['UnidadMedida'] = Relationship(back_populates='productos')
    impuesto: Optional['Impuesto'] = Relationship(back_populates='productos')
    codigoice: Optional['CodigoICE'] = Relationship(back_populates='productos')
    
    precioproductos: List['PrecioProducto'] = Relationship(back_populates='producto')
    codigobarras: List['CodigoBarras'] = Relationship(back_populates='producto')