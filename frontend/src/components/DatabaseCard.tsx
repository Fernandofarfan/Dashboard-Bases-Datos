import { Database, Activity, HardDrive, Zap } from 'lucide-react';
import type { DatabaseMetrics } from '../services/api';

interface DatabaseCardProps {
  name: string;
  type: 'postgres' | 'mysql' | 'mongodb';
  metrics: DatabaseMetrics | null;
  loading: boolean;
}

const iconMap = {
  postgres: '🐘',
  mysql: '🐬',
  mongodb: '🍃',
};

const colorMap = {
  postgres: 'bg-blue-500',
  mysql: 'bg-orange-500',
  mongodb: 'bg-green-500',
};

export const DatabaseCard = ({ name, type, metrics, loading }: DatabaseCardProps) => {
  if (loading) {
    return (
      <div className="bg-white rounded-lg shadow-md p-6 animate-pulse">
        <div className="h-4 bg-gray-200 rounded w-3/4 mb-4"></div>
        <div className="h-8 bg-gray-200 rounded w-1/2"></div>
      </div>
    );
  }

  if (!metrics || metrics.error) {
    return (
      <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-red-500">
        <h3 className="text-lg font-semibold mb-2 flex items-center gap-2">
          <span>{iconMap[type]}</span>
          {name}
        </h3>
        <p className="text-red-600">❌ Error de conexión</p>
        {metrics?.error && (
          <p className="text-sm text-gray-500 mt-2">{metrics.error}</p>
        )}
      </div>
    );
  }

  const connectionCount = 
    metrics.connections?.total || 
    metrics.connections?.current || 
    0;

  return (
    <div className={`bg-white rounded-lg shadow-md p-6 border-l-4 ${colorMap[type]} hover:shadow-lg transition-shadow`}>
      <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
        <span>{iconMap[type]}</span>
        {name}
      </h3>

      <div className="space-y-3">
        {/* Conexiones */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2 text-gray-600">
            <Activity size={16} />
            <span className="text-sm">Conexiones</span>
          </div>
          <span className="font-semibold text-gray-800">{connectionCount}</span>
        </div>

        {/* Tamaño DB */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2 text-gray-600">
            <HardDrive size={16} />
            <span className="text-sm">Tamaño</span>
          </div>
          <span className="font-semibold text-gray-800">
            {metrics.database_size_mb.toFixed(2)} MB
          </span>
        </div>

        {/* CPU */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2 text-gray-600">
            <Zap size={16} />
            <span className="text-sm">CPU</span>
          </div>
          <span className={`font-semibold ${metrics.cpu_percent > 80 ? 'text-red-600' : 'text-green-600'}`}>
            {metrics.cpu_percent.toFixed(1)}%
          </span>
        </div>

        {/* Memoria */}
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2 text-gray-600">
            <Database size={16} />
            <span className="text-sm">Memoria</span>
          </div>
          <span className={`font-semibold ${metrics.memory_percent > 85 ? 'text-red-600' : 'text-green-600'}`}>
            {metrics.memory_percent.toFixed(1)}%
          </span>
        </div>

        {/* Queries lentas (solo para Postgres y MySQL) */}
        {metrics.slow_queries !== undefined && (
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-600">Queries lentas</span>
            <span className={`font-semibold ${metrics.slow_queries > 0 ? 'text-yellow-600' : 'text-green-600'}`}>
              {metrics.slow_queries}
            </span>
          </div>
        )}

        {/* Colecciones (solo para MongoDB) */}
        {metrics.collections !== undefined && (
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-600">Colecciones</span>
            <span className="font-semibold text-gray-800">{metrics.collections}</span>
          </div>
        )}
      </div>

      <div className="mt-4 pt-4 border-t border-gray-200">
        <p className="text-xs text-gray-500">
          Última actualización: {new Date(metrics.timestamp).toLocaleTimeString()}
        </p>
      </div>
    </div>
  );
};
