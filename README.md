# Auditor Inteligente de Contratos

Sistema corporativo para el análisis, segmentación y validación de contratos legales utilizando Inteligencia Artificial (RAG) y Procesamiento de Lenguaje Natural (NLP). Proyecto desarrollado para PluriOne S.A. de C.V.

## Tecnologías y Arquitectura
- **Backend:** FastAPI, Python, SQLAlchemy, JWT (PyJWT para autenticación segura)
- **Base de Datos:** SQL Server con integración asíncrona
- **Frontend:** Vue.js, Vite, Axios
- **IA / NLP:** Azure OpenAI (GPT-4o) para extracción de cláusulas

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

## Configuración y Orden de Arranque Inicial
Sigue estos pasos en orden para levantar el proyecto desde cero:

1. **Clonar el repositorio.**
2. **Base de Datos:** Asegúrate de tener tu base de datos en SQL Server creada (`CREATE DATABASE auditoria_legal_db;`).
3. **Variables de Entorno (Backend):** Entra a la carpeta `backend/`, duplica el archivo `.env.example`, renómbralo a `.env` y llena tus credenciales (Base de datos, `SECRET_KEY`, y tus llaves de IA, ya sea de Azure OpenAI u OpenAI estándar).
4. **Entorno de Python:** Crea un entorno virtual limpio (`python -m venv venv`), actívalo (`.\venv\Scripts\activate`) y ejecuta `pip install -r requirements.txt`.
5. **Crear Administrador:** Con el entorno activado, ejecuta `python crear_admin.py`. Esto inicializará las tablas automáticamente y te pedirá crear la primera cuenta administradora.
6. **Levantar Backend:** Ejecuta `uvicorn app.main:app --reload`.
7. **Variables y Frontend:** En la carpeta `auditor-legal-frontend/`, crea un archivo `.env` con la variable `VITE_API_URL=http://localhost:8000`. Luego ejecuta `npm install` y levanta la vista con `npm run dev`.

## Guía de Uso Rápido (Flujo de Trabajo)
El flujo principal del Auditor Inteligente consta de 4 pasos:
1. **Subir:** Inicia sesión y carga un contrato en formato **PDF o DOCX** desde el panel principal.
2. **Segmentar:** El sistema procesará el documento inmediatamente y lo dividirá en cláusulas individuales.
3. **Auditar:** Ejecuta el análisis automático con IA; este proceso corre **en segundo plano** para generar tarjetas con hallazgos, riesgos y obligaciones.
4. **Preguntar:** Abre el chat integrado para hacer preguntas específicas; la IA responderá citando el nombre del contrato y la cláusula exacta de origen.