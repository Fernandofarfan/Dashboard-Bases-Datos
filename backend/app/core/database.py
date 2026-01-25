"""
Gestión de conexiones a bases de datos
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
import psycopg2
import mysql.connector
from typing import Optional, Dict, Any
import psutil
from datetime import datetime

from app.core.config import settings


class DatabaseManager:
    """Gestor de conexiones a múltiples bases de datos"""
    
    def __init__(self):
        self.connections: Dict[str, Any] = {}
    
    def test_postgres_connection(self) -> Dict[str, Any]:
        """Prueba conexión a PostgreSQL"""
        try:
            conn = psycopg2.connect(
                host=settings.POSTGRES_HOST,
                port=settings.POSTGRES_PORT,
                user=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD,
                database=settings.POSTGRES_DB
            )
            cursor = conn.cursor()
            
            # Obtener versión
            cursor.execute("SELECT version();")
            version = cursor.fetchone()[0]
            
            # Obtener métricas básicas
            cursor.execute("""
                SELECT 
                    count(*) as active_connections
                FROM pg_stat_activity
                WHERE state = 'active';
            """)
            active_conn = cursor.fetchone()[0]
            
            cursor.close()
            conn.close()
            
            return {
                "status": "connected",
                "type": "PostgreSQL",
                "version": version.split()[1],
                "active_connections": active_conn,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "status": "error",
                "type": "PostgreSQL",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def test_mysql_connection(self) -> Dict[str, Any]:
        """Prueba conexión a MySQL"""
        try:
            conn = mysql.connector.connect(
                host=settings.MYSQL_HOST,
                port=settings.MYSQL_PORT,
                user=settings.MYSQL_USER,
                password=settings.MYSQL_PASSWORD,
                database=settings.MYSQL_DB
            )
            cursor = conn.cursor()
            
            # Obtener versión
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()[0]
            
            # Obtener conexiones activas
            cursor.execute("SHOW STATUS LIKE 'Threads_connected';")
            active_conn = cursor.fetchone()[1]
            
            cursor.close()
            conn.close()
            
            return {
                "status": "connected",
                "type": "MySQL",
                "version": version,
                "active_connections": int(active_conn),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "status": "error",
                "type": "MySQL",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def test_mongo_connection(self) -> Dict[str, Any]:
        """Prueba conexión a MongoDB"""
        try:
            client = MongoClient(settings.mongo_url)
            db = client[settings.MONGO_DB]
            
            # Obtener info del servidor
            server_info = client.server_info()
            
            # Obtener estadísticas
            stats = db.command("serverStatus")
            
            client.close()
            
            return {
                "status": "connected",
                "type": "MongoDB",
                "version": server_info.get("version"),
                "active_connections": stats.get("connections", {}).get("current", 0),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {
                "status": "error",
                "type": "MongoDB",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def get_postgres_metrics(self) -> Dict[str, Any]:
        """Obtiene métricas detalladas de PostgreSQL"""
        try:
            conn = psycopg2.connect(
                host=settings.POSTGRES_HOST,
                port=settings.POSTGRES_PORT,
                user=settings.POSTGRES_USER,
                password=settings.POSTGRES_PASSWORD,
                database=settings.POSTGRES_DB
            )
            cursor = conn.cursor()
            
            # Conexiones
            cursor.execute("""
                SELECT 
                    count(*) FILTER (WHERE state = 'active') as active,
                    count(*) FILTER (WHERE state = 'idle') as idle,
                    count(*) as total
                FROM pg_stat_activity;
            """)
            conn_stats = cursor.fetchone()
            
            # Tamaño de la base de datos
            cursor.execute(f"""
                SELECT pg_database_size('{settings.POSTGRES_DB}');
            """)
            db_size = cursor.fetchone()[0]
            
            # Queries lentas (simulado)
            cursor.execute("""
                SELECT count(*) 
                FROM pg_stat_activity 
                WHERE state = 'active' 
                AND query_start < now() - interval '5 seconds';
            """)
            slow_queries = cursor.fetchone()[0]
            
            cursor.close()
            conn.close()
            
            return {
                "connections": {
                    "active": conn_stats[0],
                    "idle": conn_stats[1],
                    "total": conn_stats[2]
                },
                "database_size_mb": round(db_size / (1024 * 1024), 2),
                "slow_queries": slow_queries,
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": str(e)}
    
    def get_mysql_metrics(self) -> Dict[str, Any]:
        """Obtiene métricas detalladas de MySQL"""
        try:
            conn = mysql.connector.connect(
                host=settings.MYSQL_HOST,
                port=settings.MYSQL_PORT,
                user=settings.MYSQL_USER,
                password=settings.MYSQL_PASSWORD,
                database=settings.MYSQL_DB
            )
            cursor = conn.cursor()
            
            # Conexiones
            cursor.execute("SHOW STATUS LIKE 'Threads_connected';")
            threads_connected = int(cursor.fetchone()[1])
            
            cursor.execute("SHOW STATUS LIKE 'Threads_running';")
            threads_running = int(cursor.fetchone()[1])
            
            # Tamaño de la base de datos
            cursor.execute(f"""
                SELECT 
                    SUM(data_length + index_length) as size
                FROM information_schema.TABLES
                WHERE table_schema = '{settings.MYSQL_DB}';
            """)
            db_size = cursor.fetchone()[0] or 0
            
            # Queries lentas
            cursor.execute("SHOW STATUS LIKE 'Slow_queries';")
            slow_queries = int(cursor.fetchone()[1])
            
            cursor.close()
            conn.close()
            
            return {
                "connections": {
                    "total": threads_connected,
                    "running": threads_running
                },
                "database_size_mb": round(db_size / (1024 * 1024), 2),
                "slow_queries": slow_queries,
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": str(e)}
    
    def get_mongo_metrics(self) -> Dict[str, Any]:
        """Obtiene métricas detalladas de MongoDB"""
        try:
            client = MongoClient(settings.mongo_url)
            db = client[settings.MONGO_DB]
            
            # Estadísticas del servidor
            stats = db.command("serverStatus")
            db_stats = db.command("dbStats")
            
            client.close()
            
            return {
                "connections": {
                    "current": stats.get("connections", {}).get("current", 0),
                    "available": stats.get("connections", {}).get("available", 0)
                },
                "database_size_mb": round(db_stats.get("dataSize", 0) / (1024 * 1024), 2),
                "collections": db_stats.get("collections", 0),
                "cpu_percent": psutil.cpu_percent(interval=1),
                "memory_percent": psutil.virtual_memory().percent,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {"error": str(e)}


# Instancia global
db_manager = DatabaseManager()
