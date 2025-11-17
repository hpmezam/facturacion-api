from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importación de rutas
from app.routes.tipos_identificacion import tipos_identificacion_router
from app.routes.categorias_producto import categorias_producto_router
from app.routes.genero import genero_router
# from app.routers.producto import producto_router

app = FastAPI(title='Facturación - API')

origins = [
    'http://localhost:4200'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

prefix = '/api'
app.include_router(tipos_identificacion_router, prefix=prefix)
app.include_router(categorias_producto_router, prefix=prefix)
app.include_router(genero_router, prefix=prefix)


# app.include_router(producto_router, prefix=prefix)