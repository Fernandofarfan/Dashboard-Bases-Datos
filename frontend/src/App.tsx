import { useState, useEffect } from 'react'
import { RefreshCw } from 'lucide-react'
import './App.css'
import { apiService, type AllMetrics } from './services/api'
import { DatabaseCard } from './components/DatabaseCard'

function App() {
  const [apiStatus, setApiStatus] = useState<any>(null)
  const [metrics, setMetrics] = useState<AllMetrics | null>(null)
  const [loading, setLoading] = useState(true)
  const [refreshing, setRefreshing] = useState(false)

  const fetchData = async () => {
    setRefreshing(true)
    try {
      // Health check
      const health = await apiService.healthCheck()
      setApiStatus(health)

      // Get all metrics
      const allMetrics = await apiService.getAllMetrics()
      setMetrics(allMetrics)
    } catch (err) {
      console.error('Error fetching data:', err)
    } finally {
      setLoading(false)
      setRefreshing(false)
    }
  }

  useEffect(() => {
    fetchData()

    // Auto-refresh every 30 seconds
    const interval = setInterval(fetchData, 30000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="min-h-screen bg-gray-100">
      <header className="bg-gradient-to-r from-blue-600 to-blue-800 text-white p-6 shadow-lg">
        <div className="container mx-auto">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold">📊 Dashboard de Bases de Datos</h1>
              <p className="text-blue-100 mt-2">Monitoreo en tiempo real de tus bases de datos</p>
            </div>
            <button
              onClick={fetchData}
              disabled={refreshing}
              className="bg-white/20 hover:bg-white/30 p-3 rounded-lg transition-colors disabled:opacity-50"
              title="Actualizar métricas"
            >
              <RefreshCw size={20} className={refreshing ? 'animate-spin' : ''} />
            </button>
          </div>
        </div>
      </header>

      <main className="container mx-auto p-6">
        {/* Estado del Sistema */}
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <h2 className="text-2xl font-semibold mb-4">🚀 Estado del Sistema</h2>
          
          {apiStatus ? (
            <div className="grid md:grid-cols-2 gap-4">
              <div className="space-y-2">
                <p className="text-green-600 font-semibold flex items-center gap-2">
                  <span className="w-2 h-2 bg-green-600 rounded-full animate-pulse"></span>
                  API Conectada
                </p>
                <p className="text-sm"><strong>Versión:</strong> {apiStatus.version}</p>
                <p className="text-sm"><strong>Estado:</strong> {apiStatus.status}</p>
              </div>
              <div className="space-y-2">
                <p className="text-sm"><strong>Servicio:</strong> {apiStatus.service}</p>
                <p className="text-sm"><strong>Última actualización:</strong> {new Date().toLocaleTimeString()}</p>
              </div>
            </div>
          ) : (
            <p className="text-yellow-600 flex items-center gap-2">
              <span className="animate-spin">⏳</span>
              Conectando con la API...
            </p>
          )}
        </div>

        {/* Métricas de Bases de Datos */}
        <h2 className="text-2xl font-semibold mb-4 text-gray-800">📈 Métricas en Tiempo Real</h2>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <DatabaseCard
            name="PostgreSQL"
            type="postgres"
            metrics={metrics?.postgres || null}
            loading={loading}
          />
          <DatabaseCard
            name="MySQL"
            type="mysql"
            metrics={metrics?.mysql || null}
            loading={loading}
          />
          <DatabaseCard
            name="MongoDB"
            type="mongodb"
            metrics={metrics?.mongodb || null}
            loading={loading}
          />
        </div>

        {/* Información */}
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6">
          <h3 className="font-semibold text-blue-900 mb-2">ℹ️ Información</h3>
          <ul className="text-sm text-blue-800 space-y-1">
            <li>• Las métricas se actualizan automáticamente cada 30 segundos</li>
            <li>• Puedes forzar una actualización haciendo clic en el botón de refrescar</li>
            <li>• Los valores en rojo indican que superan los umbrales recomendados</li>
          </ul>
        </div>

        <footer className="mt-12 text-center text-gray-600 border-t pt-6">
          <p>Desarrollado por <strong>Guillermo Fernando Farfan Romero</strong></p>
          <p className="text-sm mt-2">
            <a href="https://github.com/Fernandofarfan" className="text-blue-600 hover:underline" target="_blank" rel="noopener noreferrer">
              GitHub
            </a>
            {' | '}
            <a href="https://fernandofarfan.github.io/Fernando-Farfan-Portfolio" className="text-blue-600 hover:underline" target="_blank" rel="noopener noreferrer">
              Portfolio
            </a>
            {' | '}
            <a href="mailto:fernando.farfan16@gmail.com" className="text-blue-600 hover:underline">
              Email
            </a>
          </p>
          <p className="text-xs text-gray-500 mt-2">v1.0.0 - 2026</p>
        </footer>
      </main>
    </div>
  )
}

export default App
