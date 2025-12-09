from sqlmodel import SQLModel, create_engine, Session

from app.models import categorias_producto, tipo_identificacion, tipo_persona, estado_civil, genero, persona
from app.config.seed_data import seed_data

DATABASE_URL = "sqlite:///./facturacion.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    seed_data(session)

def get_db():
    with Session(engine) as session:
        yield session