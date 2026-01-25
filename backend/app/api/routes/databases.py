"""
Endpoints para gestión de bases de datos
"""
from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

from app.core.database import db_manager

router = APIRouter()


@router.get("/test")
async def test_all_connections() -> Dict[str, Any]:
    """
    Prueba conexión a todas las bases de datos
    """
    return {
        "postgres": db_manager.test_postgres_connection(),
        "mysql": db_manager.test_mysql_connection(),
        "mongodb": db_manager.test_mongo_connection()
    }


@router.get("/postgres/connection")
async def test_postgres() -> Dict[str, Any]:
    """Prueba conexión a PostgreSQL"""
    result = db_manager.test_postgres_connection()
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["error"])
    return result


@router.get("/mysql/connection")
async def test_mysql() -> Dict[str, Any]:
    """Prueba conexión a MySQL"""
    result = db_manager.test_mysql_connection()
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["error"])
    return result


@router.get("/mongodb/connection")
async def test_mongodb() -> Dict[str, Any]:
    """Prueba conexión a MongoDB"""
    result = db_manager.test_mongo_connection()
    if result["status"] == "error":
        raise HTTPException(status_code=500, detail=result["error"])
    return result


@router.get("/postgres/metrics")
async def get_postgres_metrics() -> Dict[str, Any]:
    """Obtiene métricas de PostgreSQL"""
    metrics = db_manager.get_postgres_metrics()
    if "error" in metrics:
        raise HTTPException(status_code=500, detail=metrics["error"])
    return metrics


@router.get("/mysql/metrics")
async def get_mysql_metrics() -> Dict[str, Any]:
    """Obtiene métricas de MySQL"""
    metrics = db_manager.get_mysql_metrics()
    if "error" in metrics:
        raise HTTPException(status_code=500, detail=metrics["error"])
    return metrics


@router.get("/mongodb/metrics")
async def get_mongodb_metrics() -> Dict[str, Any]:
    """Obtiene métricas de MongoDB"""
    metrics = db_manager.get_mongo_metrics()
    if "error" in metrics:
        raise HTTPException(status_code=500, detail=metrics["error"])
    return metrics


@router.get("/metrics/all")
async def get_all_metrics() -> Dict[str, Any]:
    """Obtiene métricas de todas las bases de datos"""
    return {
        "postgres": db_manager.get_postgres_metrics(),
        "mysql": db_manager.get_mysql_metrics(),
        "mongodb": db_manager.get_mongo_metrics()
    }
