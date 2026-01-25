/**
 * Servicio de API
 */
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interfaces
export interface ConnectionStatus {
  status: string;
  type: string;
  version?: string;
  active_connections?: number;
  error?: string;
  timestamp: string;
}

export interface DatabaseMetrics {
  connections?: {
    active?: number;
    idle?: number;
    total?: number;
    current?: number;
    available?: number;
    running?: number;
  };
  database_size_mb: number;
  slow_queries?: number;
  collections?: number;
  cpu_percent: number;
  memory_percent: number;
  timestamp: string;
  error?: string;
}

export interface AllMetrics {
  postgres: DatabaseMetrics;
  mysql: DatabaseMetrics;
  mongodb: DatabaseMetrics;
}

// API Methods
export const apiService = {
  // Health check
  healthCheck: async () => {
    const response = await api.get('/health');
    return response.data;
  },

  // Test connections
  testAllConnections: async () => {
    const response = await api.get('/api/databases/test');
    return response.data;
  },

  testPostgres: async (): Promise<ConnectionStatus> => {
    const response = await api.get('/api/databases/postgres/connection');
    return response.data;
  },

  testMySQL: async (): Promise<ConnectionStatus> => {
    const response = await api.get('/api/databases/mysql/connection');
    return response.data;
  },

  testMongoDB: async (): Promise<ConnectionStatus> => {
    const response = await api.get('/api/databases/mongodb/connection');
    return response.data;
  },

  // Get metrics
  getPostgresMetrics: async (): Promise<DatabaseMetrics> => {
    const response = await api.get('/api/databases/postgres/metrics');
    return response.data;
  },

  getMySQLMetrics: async (): Promise<DatabaseMetrics> => {
    const response = await api.get('/api/databases/mysql/metrics');
    return response.data;
  },

  getMongoDBMetrics: async (): Promise<DatabaseMetrics> => {
    const response = await api.get('/api/databases/mongodb/metrics');
    return response.data;
  },

  getAllMetrics: async (): Promise<AllMetrics> => {
    const response = await api.get('/api/databases/metrics/all');
    return response.data;
  },
};

export default api;
