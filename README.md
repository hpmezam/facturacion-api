<h1 align='center'>Facturacion-api</h1>
<h3 align='center'>Software Engineer | AI, ML, DL & Computer Vision</h3>
<p align="center">
  <!-- Badges -->
  <img src="https://img.shields.io/badge/Python-3.11.9-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-0.115.12-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-3.46.1-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
</p>

Sistema backend de facturación, diseñado para empresas que requieren automatizar la emisión, 
almacenamiento y validación de comprobantes tributarios electrónicos conforme a la normativa del SRI.

## 📦 Funcionalidades principales

- 🔐 Autenticación de usuarios con JWT
- 👥 Gestión de clientes y usuarios
- 📦 Registro de productos y servicios
- 🧾 Emisión de facturas electrónicas
- 📤 Comunicación con servicios del SRI (simulado/integrable)
- 📊 Generación de reportes contables y de ventas

## 🛠️ Tecnologías utilizadas

- **Python** – Lenguaje principal para el desarrollo backend.
- **FastAPI** – Framework moderno, rápido y asíncrono para crear APIs REST.
- **SQLModel** – ORM basado en SQLAlchemy y Pydantic para manejar modelos y esquemas de base de datos.
- **SQLite** – Motor de base de datos
- **JWT (PyJWT o fastapi-jwt-auth)** – Autenticación y autorización mediante tokens JSON Web Token.
- **Alembic** – Control de versiones y migraciones de la base de datos.
- **Uvicorn** – Servidor ASGI de alto rendimiento para ejecutar la aplicación FastAPI.
- **Docker** – Plataforma de contenedorización que permite desplegar el entorno de desarrollo y producción de forma aislada, reproducible y escalable.
- **Jira** – Herramienta de gestión ágil para la planificación, seguimiento y control del desarrollo del proyecto.

## 🗂️ Estructura del proyecto

```
facturacion-api/
├── .dockerignore            # Archivos y carpetas que Docker debe ignorar
├── .gitignore               # Archivos y carpetas que Git debe ignorar
├── docker-compose.yml       # Orquestador de contenedores (app, db, etc.)
├── Dockerfile               # Configuración de la imagen Docker para FastAPI
├── facturacion.db           # Base de datos SQLite (solo para desarrollo)
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación principal
└── app/
    ├── main.py              # Punto de entrada principal de la aplicación FastAPI
    ├── config/              # Configuración de base de datos y entorno
    ├── controllers/         # Lógica de negocio (operaciones CRUD)
    ├── models/              # Modelos SQLModel (entidades de base de datos)
    ├── routes/              # Definición de endpoints y routers de la API          
    └── schemas/             # Esquemas Pydantic para validaciones
```

## 🚀 Instalación y ejecución local

1. Clona el repositorio:

```bash
git clone https://github.com/hpmezam/facturacion-api.git
cd facturacion-api
```

2. Construir la imagen y levantar los contenedores:

```bash
docker-compose up
```

3. Detener los servicios:

```bash
docker-compose down
```

## 🔒 Seguridad

- Tokens JWT con expiración.
- Encriptación de contraseñas con `bcrypt`.
- Validación de constraseñas mediante `Pydantic`.
- Middleware para control de acceso y manejo de errores.

## 🧪 Pruebas

Las pruebas unitarias y de integración se implementarán próximamente con `pytest` y `httpx` para testear los endpoints.

## 🚀 Desarrolladores
Ing. Marco Inlago
Ing. Henry Meza
Sr. Oliver Zamora