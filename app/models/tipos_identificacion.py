from sqlmodel import SQLModel, Field
from typing import Optional

class TipoIdentificacion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True, unique=True)
    nombre: str
    descripcion: Optional[str] = None
    longitud: int
    patron_regex: str
