from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer
from typing import Optional

class CodigoICE(SQLModel, table=True):
    id: Optional[int] = Field(default=None,
                              sa_column=Column(Integer, primary_key=True, autoincrement=True))
    codigo: str = Field(index=True, unique=True, max_length=100, nullable=False)
    descripcion: str = Field(max_length=200, nullable=False)
    porcentaje: float = Field(nullable=False)
    activo: bool = Field(default=True)
    
    