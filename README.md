# Auditor Inteligente de Contratos

Sistema corporativo para el análisis, segmentación y validación de contratos legales utilizando Inteligencia Artificial (RAG) y Procesamiento de Lenguaje Natural (NLP). Proyecto desarrollado para PluriOne S.A. de C.V.

## Tecnologías y Arquitectura
* **Backend:** FastAPI, Python, SQLAlchemy, JWT (PyJWT para autenticación segura)
* **Base de Datos:** SQL Server con integración asíncrona
* **Frontend:** Vue.js, Vite, Axios
* **IA / NLP:** Azure OpenAI (GPT-4o) para extracción de cláusulas

## 🗄️ Requisitos del Sistema y Configuración de Base de Datos

Para que el backend asíncrono funcione correctamente con SQL Server, es obligatorio contar con los siguientes componentes en el entorno:

1. **ODBC Driver 17 for SQL Server:** 
   - Asegúrate de tener instalado el controlador oficial de Microsoft. Puedes descargarlo desde la [página oficial de Microsoft](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).
2. **Creación de la Base de Datos:**
   - Abre SQL Server Management Studio (SSMS) o tu cliente de preferencia y ejecuta la siguiente sentencia SQL para crear la base de datos que utiliza el proyecto:
     ```sql
     CREATE DATABASE auditoria_legal_db;
     GO
     ```
     
3. **Variables de Entorno:**
   - Copia el archivo `backend/.env.example` a un archivo `.env` dentro de la carpeta `backend/` y configura tu cadena de conexión y credenciales de Azure OpenAI.

## Configuración del Entorno Local
1. Clonar el repositorio.
2. En la carpeta `backend/`, duplicar `.env.example`, renombrarlo a `.env` y llenar las credenciales (Azure, BD y `SECRET_KEY`).
3. En la carpeta `auditor-legal-frontend/`, crear un archivo `.env` con la variable `VITE_API_URL=http://localhost:8000`.
4. Instalar dependencias del backend (`pip install -r requirements.txt`) y levantar el servidor (`uvicorn app.main:app --reload`).
5. Instalar dependencias del frontend (`npm install`) y levantar la vista (`npm run dev`).



> **Nota de Seguridad:** Por requerimientos del proyecto, el registro público de usuarios se encuentra deshabilitado. La creación de cuentas y asignación de accesos es controlada exclusivamente por el departamento de IT de la empresa a través de la base de datos.