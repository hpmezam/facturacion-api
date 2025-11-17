from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Importación de rutas
from app.routes.tipos_identificacion import tipos_identificacion_router
from app.routes.categorias_producto import categorias_producto_router
from app.routes.unidades_medida import unidades_medida_router
from app.routes.impuestos import impuestos_router
from app.routes.codigos_ice import codigos_ice_router
from app.routes.productos import productos_router
from app.routes.precios_productos import precios_productos_router
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
app.include_router(unidades_medida_router, prefix=prefix)
app.include_router(impuestos_router, prefix=prefix)
app.include_router(codigos_ice_router, prefix=prefix)
app.include_router(productos_router, prefix=prefix)
app.include_router(precios_productos_router, prefix=prefix)


# app.include_router(producto_router, prefix=prefix)