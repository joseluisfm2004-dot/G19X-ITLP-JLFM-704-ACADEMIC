# Auditor Inteligente de Contratos

Sistema corporativo para el análisis, segmentación y validación de contratos legales utilizando Inteligencia Artificial (RAG) y Procesamiento de Lenguaje Natural (NLP). Proyecto desarrollado para PluriOne S.A. de C.V.

## Tecnologías y Arquitectura
* **Backend:** FastAPI, Python, SQLAlchemy, JWT (PyJWT para autenticación segura)
* **Base de Datos:** SQL Server con integración asíncrona
* **Frontend:** Vue.js, Vite, Axios
* **IA / NLP:** Azure OpenAI (GPT-4o) para extracción de cláusulas

## Configuración del Entorno Local
1. Clonar el repositorio.
2. En la carpeta `backend/`, duplicar `.env.example`, renombrarlo a `.env` y llenar las credenciales (Azure, BD y `SECRET_KEY`).
3. En la carpeta `auditor-legal-frontend/`, crear un archivo `.env` con la variable `VITE_API_URL=http://localhost:8000`.
4. Instalar dependencias del backend (`pip install -r requirements.txt`) y levantar el servidor (`uvicorn app.main:app --reload`).
5. Instalar dependencias del frontend (`npm install`) y levantar la vista (`npm run dev`).

> **Nota de Seguridad:** Por requerimientos del proyecto, el registro público de usuarios se encuentra deshabilitado. La creación de cuentas y asignación de accesos es controlada exclusivamente por el departamento de IT de la empresa a través de la base de datos.