from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import Column, Integer


class Impuesto(SQLModel, table=True):
    id: Optional[int] = Field(default=None,
                              sa_column=Column(Integer, primary_key=True, autoincrement=True))
    codigo_sri: str = Field(index=True, max_length=100, nullable=False)
    nombre: str = Field(index=True, max_length=100, nullable=False)
    porcentaje: float = Field(nullable=False)
    descripcion: str = Field(max_length=200, nullable=False)
    activo: bool = Field(default=True)