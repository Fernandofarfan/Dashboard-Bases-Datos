"""
Dashboard de Bases de Datos - API Backend
Autor: Guillermo Fernando Farfan Romero
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api.routes import api_router
from app.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gestión del ciclo de vida de la aplicación"""
    # Startup
    print("🚀 Iniciando Dashboard de Bases de Datos...")
    print(f"📊 Ambiente: {settings.APP_ENV}")
    yield
    # Shutdown
    print("👋 Cerrando Dashboard de Bases de Datos...")

# Crear aplicación FastAPI
app = FastAPI(
    title="Dashboard de Bases de Datos",
    description="API para monitoreo en tiempo real de bases de datos",
    version="1.0.0",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de prueba
@app.get("/")
async def root():
    """Endpoint raíz de la API"""
    return {
        "message": "Dashboard de Bases de Datos API",
        "version": "1.0.0",
        "status": "active",
        "docs": "/docs",
        "environment": settings.APP_ENV
    }

@app.get("/health")
async def health_check():
    """Health check del servicio"""
    return {
        "status": "healthy",
        "service": "dashboard-db-api"
    }

# Incluir routers
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
