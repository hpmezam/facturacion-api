from sqlmodel import SQLModel, create_engine, Session

from app.models import categorias_producto, tipos_identificacion,empresas,establecimientos,certificados_digitales

DATABASE_URL = "sqlite:///./facturacion.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session