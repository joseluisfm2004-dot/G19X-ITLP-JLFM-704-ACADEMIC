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

## Configuración del Entorno Local
1. Clonar el repositorio.
2. En la carpeta `backend/`, duplicar `.env.example`, renombrarlo a `.env` y llenar las credenciales (Azure, BD y `SECRET_KEY`).
3. En la carpeta `auditor-legal-frontend/`, crear un archivo `.env` con la variable `VITE_API_URL=http://localhost:8000`.
4. Instalar dependencias del backend (`pip install -r requirements.txt`) y levantar el servidor (`uvicorn app.main:app --reload`).
5. Instalar dependencias del frontend (`npm install`) y levantar la vista (`npm run dev`).

---

## 🔐 Creación del Primer Administrador (Nota de Seguridad)

Por requerimientos del proyecto, el registro público de usuarios se encuentra deshabilitado. La creación de la primera cuenta administradora para el departamento de IT se realiza a través de un script seguro por consola.

Con tu entorno virtual activado y la base de datos corriendo, ejecuta en la raíz de `backend/`:

```bash
python crear_admin.py
```
El script te solicitará tu nombre, correo y una contraseña segura. Una vez creado el perfil, utiliza estas credenciales para iniciar sesión en el frontend.

---

## 🤖 Declaración de Uso de Inteligencia Artificial

Para el desarrollo, estructuración y optimización de este proyecto académico, se utilizó asistencia de Inteligencia Artificial (modelos LLM) como herramienta de *pair programming*, generación de componentes repetitivos, depuración de código asíncrono y redacción de documentación técnica. 

Toda la arquitectura, lógica de negocio y ensamblaje final fueron revisados y validados manualmente para garantizar el cumplimiento de los estándares de ingeniería de software requeridos.

## Orden de Arranque Inicial
Para la primera ejecución del proyecto, sigue este orden exacto para inicializar la base de datos y tu usuario maestro:
1. Asegúrate de tener tu base de datos en SQL Server creada y las credenciales en tu archivo `.env`.
2. Entra a la carpeta backend, activa tu entorno virtual y ejecuta python crear_admin.py. Esto inicializará las tablas automáticamente y te pedirá crear el primer administrador.
3. Levanta el servidor del backend (`uvicorn app.main:app --reload`).
4. Levanta el servidor del frontend (`npm run dev`).

## Guía de Uso Rápido (Flujo de Trabajo)
El flujo principal del Auditor Inteligente consta de 4 pasos:
1. **Subir:** Inicia sesión y carga un contrato en formato PDF desde el panel principal.
2. **Segmentar:** El sistema procesará el documento en segundo plano y lo dividirá en cláusulas individuales.
3. **Auditar:** Ejecuta el análisis automático con IA (Azure GPT-4o) para generar tarjetas con hallazgos, riesgos y obligaciones.
4. **Preguntar:** Abre el chat integrado para hacer preguntas específicas; la IA responderá citando el nombre del contrato y la cláusula exacta de origen.