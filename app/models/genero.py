from sqlmodel import SQLModel, Field
from typing import Optional

class Genero(SQLModel, table=True):   
    __tablename__ = "genero"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=30, nullable=False)
    activo: bool