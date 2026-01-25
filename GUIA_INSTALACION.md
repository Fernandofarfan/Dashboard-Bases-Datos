# 🚀 Guía de Instalación - Dashboard de Bases de Datos

## 📋 Requisitos Previos

- **Python 3.11+**
- **Node.js 18+**
- **Docker & Docker Compose** (opcional, pero recomendado)

---

## 🐳 Opción 1: Instalación con Docker (Recomendada)

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/Fernandofarfan/Dashboard-Bases-Datos.git
cd Dashboard-Bases-Datos
```

### Paso 2: Levantar servicios
```bash
docker-compose up --build
```

Esto levantará:
- ✅ Backend API (Puerto 8000)
- ✅ Frontend React (Puerto 5173)
- ✅ PostgreSQL (Puerto 5432)
- ✅ MySQL (Puerto 3306)
- ✅ MongoDB (Puerto 27017)

### Paso 3: Acceder a la aplicación
- **Frontend:** http://localhost:5173
- **API Docs:** http://localhost:8000/docs
- **API Health:** http://localhost:8000/health

---

## 💻 Opción 2: Instalación Local

### Backend

#### 1. Navegar a la carpeta backend
```bash
cd backend
```

#### 2. Crear entorno virtual
```bash
python -m venv venv
```

#### 3. Activar entorno virtual
**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

#### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 5. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus credenciales de bases de datos
```

#### 6. Iniciar servidor
```bash
python main.py
```

El backend estará disponible en: http://localhost:8000

---

### Frontend

#### 1. Navegar a la carpeta frontend (nueva terminal)
```bash
cd frontend
```

#### 2. Instalar dependencias
```bash
npm install
```

#### 3. Configurar variables de entorno
```bash
cp .env.example .env
# Por defecto apunta a http://localhost:8000
```

#### 4. Iniciar servidor de desarrollo
```bash
npm run dev
```

El frontend estará disponible en: http://localhost:5173

---

## ⚙️ Configuración de Bases de Datos

### PostgreSQL

Crear base de datos de prueba:
```sql
CREATE DATABASE testdb;
```

### MySQL

Crear base de datos de prueba:
```sql
CREATE DATABASE testdb;
```

### MongoDB

No requiere configuración adicional si usas Docker.

---

## 🧪 Verificar Instalación

1. **Backend Health Check:**
```bash
curl http://localhost:8000/health
```

2. **Probar conexiones:**
```bash
curl http://localhost:8000/api/databases/test
```

3. **Obtener métricas:**
```bash
curl http://localhost:8000/api/databases/metrics/all
```

---

## 🐛 Troubleshooting

### Error: "Connection refused"
- Verifica que las bases de datos estén corriendo
- Revisa las credenciales en `.env`
- Verifica los puertos no estén ocupados

### Error: "Module not found"
- Backend: Asegúrate de estar en el entorno virtual y que las dependencias estén instaladas
- Frontend: Ejecuta `npm install` nuevamente

### Error: "CORS"
- Verifica que el frontend esté configurado para apuntar al backend correcto
- Revisa la configuración de CORS en `backend/main.py`

---

## 📚 Documentación Adicional

- **API Docs:** http://localhost:8000/docs
- **README:** [README.md](README.md)
- **Changelog:** [CHANGELOG.md](CHANGELOG.md)

---

## 🆘 Soporte

¿Problemas con la instalación?

- **Email:** fernando.farfan16@gmail.com
- **GitHub Issues:** [Reportar problema](https://github.com/Fernandofarfan/Dashboard-Bases-Datos/issues)

---

Desarrollado con ❤️ por [Guillermo Fernando Farfan Romero](https://fernandofarfan.github.io/Fernando-Farfan-Portfolio)
