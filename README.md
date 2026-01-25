# 📊 Dashboard de Bases de Datos

Sistema de monitoreo en tiempo real para bases de datos relacionales y NoSQL.

## 🎯 Características

- ✅ Monitoreo en tiempo real de múltiples bases de datos
- 📊 Dashboard interactivo con métricas clave
- 🔔 Sistema de alertas automáticas
- 📈 Análisis de queries lentas
- 💾 Optimizaciones sugeridas
- 📄 Reportes automatizados
- 🐳 Desplegable con Docker

## 🛠️ Stack Tecnológico

### Backend
- **Python 3.11+**
- **FastAPI** - Framework web moderno y rápido
- **SQLAlchemy** - ORM para bases de datos
- **Pydantic** - Validación de datos
- **APScheduler** - Tareas programadas

### Frontend
- **React 18+**
- **TypeScript**
- **Vite** - Build tool
- **TanStack Query** - Gestión de estado servidor
- **Recharts** - Visualización de datos
- **Tailwind CSS** - Estilos

### Bases de Datos Soportadas
- PostgreSQL
- MySQL
- SQL Server
- MongoDB

### DevOps
- Docker & Docker Compose
- GitHub Actions (CI/CD)

## 📁 Estructura del Proyecto

```
Dashboard-Bases-Datos/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── services/
│   │   └── utils/
│   ├── tests/
│   ├── requirements.txt
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── types/
│   ├── package.json
│   └── vite.config.ts
├── docker-compose.yml
└── README.md
```

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.11+
- Node.js 18+
- Docker & Docker Compose (opcional)

### Instalación Local

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Con Docker
```bash
docker-compose up --build
```

## 📊 Métricas Monitoreadas

- **Conexiones Activas**
- **CPU y Memoria de la BD**
- **Espacio en Disco**
- **Queries Lentas**
- **Deadlocks**
- **Índices sin uso**
- **Tiempo de Respuesta**

## 🔔 Sistema de Alertas

- Query execution time > umbral
- Espacio en disco < 10%
- Conexiones activas > 80% del máximo
- Deadlocks detectados
- Servicios caídos

## 📈 Roadmap

### v1.0 (Actual)
- [x] Estructura base del proyecto
- [ ] Backend API con FastAPI
- [ ] Conexión a PostgreSQL y MySQL
- [ ] Dashboard básico en React
- [ ] Métricas en tiempo real

### v1.1
- [ ] Soporte para MongoDB
- [ ] Sistema de alertas por email
- [ ] Reportes en PDF
- [ ] Autenticación JWT

### v2.0
- [ ] Machine Learning para predicción
- [ ] Optimizaciones automáticas
- [ ] Multi-tenant
- [ ] API REST pública

## 👨‍💻 Autor

**Guillermo Fernando Farfan Romero**

- Portfolio: [fernandofarfan.github.io](https://fernandofarfan.github.io/Fernando-Farfan-Portfolio)
- GitHub: [@Fernandofarfan](https://github.com/Fernandofarfan)
- LinkedIn: [guillermo-farfan](https://www.linkedin.com/in/fernando-farfan-01ba68143)
- Email: fernando.farfan16@gmail.com

## 📄 Licencia

MIT License - ver [LICENSE](LICENSE) para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea tu feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: nueva funcionalidad'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

⭐ Si este proyecto te resulta útil, no olvides darle una estrella en GitHub
