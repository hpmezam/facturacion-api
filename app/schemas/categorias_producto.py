from sqlmodel import SQLModel, Field
from typing import Optional

class CategoriaProductoBase(SQLModel):
    nombre: str
    descripcion: Optional[str] = None
    codigo_sri: str
    activo: bool = True

class CategoriaProductoCreate(CategoriaProductoBase):
    pass

class CategoriaProductoRead(CategoriaProductoBase):
    pass

class CategoriaProductoUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    codigo_sri: Optional[str] = None
    activo: Optional[bool] = None


    