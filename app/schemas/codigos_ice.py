from sqlmodel import SQLModel, Field
from typing import Optional

class CodigoICE(SQLModel):
    codigo: str
    descripcion: str
    porcentaje: float
    activo: bool = True

class CodigoICECreate(CodigoICE):
    pass

class CodigoICERead(CodigoICE):
    id:int
    pass

class CodigoICEUpdate(SQLModel):
    codigo: Optional[str] = None
    descripcion: Optional[str] = None
    porcentaje: Optional[float] = None
    activo: Optional[bool] = None
    

    