from sqlmodel import Session, select
from app.models.tipo_persona import TipoPersona
from app.models.tipo_identificacion import TipoIdentificacion
from app.models.estado_civil import EstadoCivil
from app.models.genero import Genero

def seed_data(db: Session):
    # ---- TIPOS DE PERSONA ----
    tipos_persona = [
        {"nombre": "NATURAL", "activo": True},
        {"nombre": "JURIDICA", "activo": True},
    ]
    
    for tipo in tipos_persona:
        existe = db.exec(select(TipoPersona).where(TipoPersona.nombre == tipo["nombre"])).first()
        if not existe:
            nuevo_tipo = TipoPersona(**tipo)
            db.add(nuevo_tipo)
            
    # ---- TIPOS DE IDENTIFICACIÓN ----
    tipos_identificacion = [
        {"nombre": "Cédula", "descripcion": "Documento nacional de identidad", "longitud": 10, "activo": True},
        {"nombre": "RUC", "descripcion": "Registro Único de Contribuyentes", "longitud": 13, "activo": True},
    ]
    
    for tipo in tipos_identificacion:
        existe = db.exec(select(TipoIdentificacion).where(TipoIdentificacion.nombre == tipo["nombre"])).first()
        if not existe:
            nuevo_tipo = TipoIdentificacion(**tipo)
            db.add(nuevo_tipo)
            
    # ---- ESTADO CIVIL ----
    estados_civil = [
        {"nombre": "SOLTERO", "activo": True},
        {"nombre": "CASADO", "activo": True},
        {"nombre": "DIVORCIADO", "activo": True},
        {"nombre": "VIUDO", "activo": True},
    ]
    
    for estado in estados_civil:
        existe = db.exec(select(EstadoCivil).where(EstadoCivil.nombre == estado["nombre"])).first()
        if not existe:
            nuevo_estado = EstadoCivil(**estado)
            db.add(nuevo_estado)
            
    # ---- GENERO ----
    generos = [
        {"nombre": "MASCULINO", "activo": True},
        {"nombre": "FEMENINO", "activo": True},
    ]
    
    for genero in generos:
        existe = db.exec(select(Genero).where(Genero.nombre == genero["nombre"])).first()
        if not existe:
            nuevo_genero = Genero(**genero)
            db.add(nuevo_genero)
    
    db.commit()