from sqlmodel import SQLModel, Field
from typing import Optional
from decimal import Decimal

class CodigoICE(SQLModel):
    codigo: str
    descripcion: str
    porcentaje: Decimal
    activo: bool = True

class CodigoICECreate(CodigoICE):
    pass

class CodigoICERead(CodigoICE):
    id:int
    pass

class CodigoICEUpdate(SQLModel):
    codigo: Optional[str] = None
    descripcion: Optional[str] = None
    porcentaje: Optional[Decimal] = None
    activo: Optional[bool] = None
    

    