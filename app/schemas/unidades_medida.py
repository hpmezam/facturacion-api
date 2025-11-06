from sqlmodel import SQLModel, Field
from typing import Optional

class UnidadMedida(SQLModel):
    codigo: str
    nombre: str
    simbolo: str
    activo: bool = True

class UnidadMedidaCreate(UnidadMedida):
    pass

class UnidadMedidaRead(UnidadMedida):
    id: int
    pass

class UnidadMedidaUpdate(SQLModel):
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    simbolo: Optional[str] = None
    activo: Optional[bool] = None
    
