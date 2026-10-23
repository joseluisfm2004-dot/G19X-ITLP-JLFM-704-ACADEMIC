# Auditor Inteligente de Contratos - Frontend

Este es el cliente web para el sistema de Auditoría de Contratos, construido con **Vue 3** y **Vite**. Proporciona la interfaz gráfica para la carga de documentos, visualización del historial, segmentación, y un chat interactivo impulsado por IA (RAG).

## Requisitos Previos
- [Node.js](https://nodejs.org/) (v16 o superior)
- NPM o Yarn

## Configuración Inicial

1. **Instalar dependencias:**
```bash
npm install
```

2. **Variables de Entorno:**
Copia el archivo de ejemplo y asegúrate de que apunte a tu backend local:
```bash
cp .env.example .env
```
*(Debe contener `VITE_API_URL=http://localhost:8000`)*

3. **Ejecutar en entorno de desarrollo:**
```bash
npm run dev
```

## Tecnologías Principales
* Vue 3 (Composition API)
* Vite
* Axios (Peticiones HTTP al backend)
* html2pdf.js (Exportación de reportes)