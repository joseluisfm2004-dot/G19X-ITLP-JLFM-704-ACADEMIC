<template>
  <div class="dashboard-layout">
    <header class="navbar">
      <div class="nav-brand">
        <svg xmlns="http://www.w3.org/2000/svg" class="brand-shield" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
        </svg>
        <div class="brand-titles">
          <h1>Auditor Inteligente de Contratos</h1>
          <span class="brand-company">PluriOne S.A. de C.V.</span>
        </div>
      </div>
      
      <div class="nav-controls">
        <button @click="abrirBuscador" class="nav-action-btn" title="Buscar detalles por ID">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="btn-icon">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <span class="nav-text">Buscar ID</span>
        </button>

        <button @click="mostrarModalPerfil = true" class="nav-action-btn" title="Ver Perfil">
          <div class="profile-avatar">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
            </svg>
          </div>
          <span class="nav-text">Mi Perfil</span>
        </button>

        <button @click="cerrarSesion" class="logout-btn">
          <svg xmlns="http://www.w3.org/2000/svg" class="btn-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          Salir
        </button>
      </div>
    </header>

    <main class="main-content">
      <div class="welcome-banner">
        <h2>Panel de Control Ejecutivo</h2>
        <p>Gestión automatizada de contratos e inteligencia artificial RAG para auditoría de riesgos jurídicos.</p>
      </div>
      
      <div class="tabs-container">
        <button @click="vistaActual = 'carga'" :class="['tab-btn', vistaActual === 'carga' ? 'active' : '']">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
          Cargar Contrato
        </button>
        <button @click="vistaActual = 'gestion'" :class="['tab-btn', vistaActual === 'gestion' ? 'active' : '']">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
          Gestión y Auditoría
        </button>
        <button @click="vistaActual = 'chat'" :class="['tab-btn', vistaActual === 'chat' ? 'active' : '']">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" /></svg>
          Asistente IA (Chat)
        </button>
      </div>

      <div v-if="vistaActual === 'carga'" class="view-section">
        <div class="card upload-section">
          <div class="card-title-area">
            <div class="card-icon blue">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
              </svg>
            </div>
            <div>
              <h3>Carga de Nuevo Contrato</h3>
              <p>Sube un documento en formato digital para iniciar el pipeline de auditoría</p>
            </div>
          </div>

          <div class="upload-form">
            <div class="input-group">
              <label>Título o Identificador del Contrato</label>
              <input 
                type="text" 
                v-model="tituloContrato" 
                placeholder="Ej. Contrato de Servicios PluriOne 2026" 
                class="text-input" 
              />
            </div>

            <div class="upload-controls">
              <div class="file-drop-zone">
                <input type="file" @change="seleccionarArchivo" accept=".pdf,.docx" class="file-input" id="file-upload" />
                <label for="file-upload" class="file-label">
                  <span class="file-name-display">{{ archivoSeleccionado ? archivoSeleccionado.name : 'Seleccionar archivo PDF o Word...' }}</span>
                  <span class="browse-badge">Explorar</span>
                </label>
              </div>
              
              <button @click="subirContrato" :disabled="!archivoSeleccionado || !tituloContrato || subiendo" class="upload-btn">
                <span v-if="subiendo" class="spinner"></span>
                {{ subiendo ? 'Procesando...' : 'Subir y Registrar' }}
              </button>
            </div>
          </div>
          <div v-if="mensaje" :class="['alert-message', error ? 'error' : 'success']">
            {{ mensaje }}
          </div>
        </div>
      </div>

      <div v-if="vistaActual === 'gestion'" class="view-section">
        <div class="card">
          <div class="card-title-area">
            <div class="card-icon slate">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <div>
              <h3>Contratos Registrados</h3>
              <p>Historial de documentos institucionales listos para segmentación y auditoría</p>
            </div>
          </div>
          
          <div v-if="cargandoContratos" class="empty-state">
            <div class="spinner dark"></div>
            <span>Cargando contratos del sistema...</span>
          </div>
          
          <div v-else-if="contratos.length === 0" class="empty-state">
            No hay contratos registrados actualmente. Ve a la pestaña "Cargar Contrato".
          </div>

          <div v-else class="table-responsive">
            <table class="contracts-table">
              <thead>
                <tr>
                  <th>ID</th>
                  <th>Título del Contrato</th>
                  <th>Nombre del Archivo</th>
                  <th>Estado</th>
                  <th class="text-center">Acciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="c in contratos" :key="c.id" :class="{'row-selected': contratoSeleccionadoId === c.id}">
                  <td><span class="id-tag">#{{ c.id }}</span></td>
                  <td><strong>{{ c.titulo }}</strong></td>
                  <td class="file-cell">{{ c.nombre_archivo }}</td>
                  <td>
                    <span :class="['badge', c.estado]">{{ c.estado }}</span>
                  </td>
                  <td class="action-buttons-cell">
                    <button type="button" @click.prevent="procesarContrato(c.id)" class="action-btn segment-btn" title="Segmentar cláusulas">
                      Segmentar
                    </button>
                    <button @click="auditarContrato(c.id)" :disabled="auditando" class="action-btn audit-btn" title="Ejecutar Auditoría con Azure OpenAI">
                      {{ auditando && contratoSeleccionadoId === c.id ? 'Auditando...' : 'Auditar con IA' }}
                    </button>
                   <button 
                      v-if="c.estado && (c.estado.toLowerCase().includes('auditado') || c.estado.toLowerCase().includes('completada'))"
                      @click="descargarPdfSeguro(c.id)"
                          class="action-btn download-btn-table"
                       title="Descargar Reporte PDF"
                           style="background-color: #2b6cb0; border: none; cursor: pointer;"
                      >
                      📄 PDF
                      </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div v-if="resultadoAuditoria && vistaActual === 'gestion'" class="card audit-results-section" ref="reportePDF">
          <div class="audit-header">
            <div class="card-title-area mb-0">
              <div class="card-icon purple">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
                </svg>
              </div>
              <div>
                <h3>Reporte de Auditoría Inteligente</h3>
                <p>Evaluación de riesgos y cumplimiento normativo generada por GPT-4o</p>
              </div>
            </div>
            
            <div class="header-actions">
              <button @click="descargarPDF" class="action-btn download-btn">
                📄 Descargar Reporte PDF
              </button>
              <div :class="['risk-score-badge', obtenerClaseRiesgoGlobal(resultadoAuditoria.puntaje_riesgo)]">
                Riesgo Global: {{ resultadoAuditoria.puntaje_riesgo.toFixed(1) }} / 100
              </div>
            </div>
          </div>

          <div class="executive-summary">
            <strong>Resumen Ejecutivo:</strong>
            <p>{{ resultadoAuditoria.resumen_ejecutivo }}</p>
          </div>

          <h4 class="section-subtitle">Hallazgos Detectados ({{ resultadoAuditoria.total_hallazgos }})</h4>
          
          <div v-if="resultadoAuditoria.hallazgos.length === 0" class="empty-state">
            ¡Excelente! No se detectaron riesgos jurídicos significativos en este contrato.
          </div>

          <div v-else class="findings-list">
            <div v-for="(h, index) in resultadoAuditoria.hallazgos" :key="index" class="finding-card">
              <div class="finding-top">
                <span class="finding-clause">Cláusula {{ h.numero_clausula }}: {{ h.titulo_clausula }}</span>
                <span :class="['badge', obtenerClaseBadgeRiesgo(h.nivel_riesgo)]">
                  {{ h.nivel_riesgo }} - {{ h.tipo }}
                </span>
              </div>
              <p class="finding-desc"><strong>Descripción:</strong> {{ h.descripcion }}</p>
              <p class="finding-sug"><strong>Sugerencia de Mejora:</strong> {{ h.sugerencia_mejora }}</p>
            </div>
          </div>
        </div>
      </div>

      <div v-if="vistaActual === 'chat'" class="chat-layout">
        
        <aside class="chat-sidebar">
          <div class="sidebar-header">
            <span class="sidebar-title">Todas las consultas</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="filter-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z" />
            </svg>
          </div>
          
          <ul class="chat-list">
            <li v-if="contratos.length === 0" class="chat-list-empty">
              Sube un contrato para iniciar el chat.
            </li>
            <li 
              v-for="c in contratos" 
              :key="c.id" 
              @click="seleccionarContratoChat(c)"
              :class="['chat-list-item', contratoSeleccionadoId === c.id ? 'active' : '']"
            >
              {{ c.titulo }}
            </li>
          </ul>
        </aside>

        <main class="chat-main">
          <div v-if="!contratoSeleccionadoId" class="chat-placeholder">
            <svg xmlns="http://www.w3.org/2000/svg" class="chat-placeholder-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
            </svg>
            <h3>Asistente Legal RAG</h3>
            <p>Selecciona un contrato del panel lateral para consultar el historial o iniciar una nueva conversación sobre el documento.</p>
          </div>
          
          <div v-else class="chat-active-container">
            <div class="chat-header">
              <h3>Consulta: {{ contratoVisualizado?.titulo || contratoSeleccionadoChat?.titulo }}</h3>
            </div>
            
            <div class="chat-history-area" ref="chatHistoryRef">
              <div v-if="chatMensajes.length === 0" class="empty-chat-state">
                <p>Escribe tu consulta jurídica. El asistente tiene el contexto de este contrato.</p>
              </div>
              
              <div v-for="(msg, idx) in chatMensajes" :key="idx" :class="['chat-bubble-wrapper', msg.rol]">
                <div class="chat-bubble">
                  <span class="bubble-author">{{ msg.rol === 'user' ? 'Tú (Auditor)' : 'IA Azure GPT-4o' }}</span>
                  <p>{{ msg.texto }}</p>
                  
                  <div v-if="msg.citas && msg.citas.length > 0" class="chat-citations">
                    <span class="citations-title">Fuentes consultadas:</span>
                    <ul>
                      <li v-for="(cita, i) in msg.citas" :key="i">📄 {{ cita }}</li>
                    </ul>
                  </div>
                </div>
              </div>
              
              <div v-if="enviandoMensaje" class="chat-bubble-wrapper ia">
                <div class="chat-bubble">
                  <span class="bubble-author">IA Azure GPT-4o</span>
                  <div class="typing-indicator">
                    <span></span><span></span><span></span>
                  </div>
                </div>
              </div>
            </div>

            <div class="chat-input-area">
              <input 
                type="text" 
                v-model="mensajeActual" 
                @keyup.enter="enviarMensajeChat"
                placeholder="Escribe un mensaje para continuar la conversación..." 
                class="text-input chat-input-field" 
                :disabled="enviandoMensaje"
              />
              <button @click="enviarMensajeChat" :disabled="!mensajeActual.trim() || enviandoMensaje" class="upload-btn chat-send-btn">
                <svg xmlns="http://www.w3.org/2000/svg" class="send-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
                </svg>
              </button>
            </div>
          </div>
        </main>
      </div>

    </main>

   
    <div v-if="mostrarModalBuscador" class="fixed-modal-overlay">
      <div class="modal-content">
        <div class="modal-header">
          <h3>Buscar Contrato por ID</h3>
          <button @click="mostrarModalBuscador = false" class="close-modal-btn">&times;</button>
        </div>
        <div class="modal-body">
          <div class="input-group" style="margin-bottom: 1rem;">
            <label>Ingresa el ID del contrato</label>
            <div style="display: flex; gap: 0.5rem;">
              <input 
                type="number" 
                v-model="inputBusquedaId" 
                placeholder="Ej. 12" 
                class="text-input" 
                @keyup.enter="ejecutarBusqueda"
              />
              <button @click="ejecutarBusqueda" class="upload-btn">Buscar</button>
            </div>
          </div>

          <div v-if="errorBusqueda" class="alert-message error">
            {{ errorBusqueda }}
          </div>

          <div v-if="contratoVisualizado && !errorBusqueda" class="contract-details-grid" style="margin-top: 1.5rem; background: #f8fafc; padding: 1rem; border-radius: 8px; border: 1px solid #e2e8f0;">
            <div class="detail-row">
              <strong>ID de Sistema:</strong> <span>#{{ contratoVisualizado.id }}</span>
            </div>
            <div class="detail-row">
              <strong>Título:</strong> <span>{{ contratoVisualizado.titulo }}</span>
            </div>
            <div class="detail-row">
              <strong>Nombre del Archivo:</strong> <span class="file-cell">{{ contratoVisualizado.nombre_archivo }}</span>
            </div>
            <div class="detail-row">
              <strong>Estado Actual:</strong> <span :class="['badge', contratoVisualizado.estado]">{{ contratoVisualizado.estado }}</span>
            </div>
            <div class="detail-row">
              <strong>Ubicación de Servidor:</strong> 
              <span class="code-path">/uploads/contratos/{{ contratoVisualizado.nombre_archivo }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="mostrarModalPerfil" class="fixed-modal-overlay">
      <div class="modal-content text-gray-800">
        <div class="modal-header">
          <h3>Información del Perfil</h3>
          <button @click="mostrarModalPerfil = false" class="close-modal-btn">&times;</button>
        </div>
        <div class="modal-body">
          <div class="profile-info-grid">
            <div class="info-item">
              <span class="info-label">Nombre / Rol:</span>
              <strong>{{ perfilUsuario ? perfilUsuario.nombre + ' / ' + perfilUsuario.rol : 'Cargando...' }}</strong>
            </div>
            <div class="info-item">
              <span class="info-label">Empresa:</span>
              <strong>PluriOne S.A. de C.V.</strong>
            </div>
            <div class="info-item">
              <span class="info-label">Estado de Cuenta:</span>
              <span class="badge riesgo-bajo">{{ perfilUsuario ? 'Activo / Validado' : 'Cargando...' }}</span>
            </div>
            <div class="info-item">
              <span class="info-label">Privilegios:</span>
              <span>{{ perfilUsuario && perfilUsuario.rol === 'admin' ? 'Auditoría RAG (GPT-4o), Segmentación, Carga' : 'Segmentación, Carga' }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { useAuthStore } from '../stores/auth'; 
import { useRouter } from 'vue-router';
import axios from 'axios';
import html2pdf from 'html2pdf.js';

const authStore = useAuthStore();
const router = useRouter();


const vistaActual = ref('carga'); 
const mostrarModalPerfil = ref(false);
const mostrarModalBuscador = ref(false);
const inputBusquedaId = ref('');
const errorBusqueda = ref('');
const contratoVisualizado = ref(null);

const perfilUsuario = ref(null);

const cargarPerfil = async () => {
  try {
    const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/v1/usuarios/me`, {
      headers: { 'Authorization': `Bearer ${authStore.token}` }
    });
    perfilUsuario.value = response.data;
  } catch (err) {
    console.error("Error al obtener el perfil:", err);
  }
};

const tituloContrato = ref('');
const archivoSeleccionado = ref(null);
const subiendo = ref(false);
const mensaje = ref('');
const error = ref(false);

const contratos = ref([]);
const cargandoContratos = ref(false);
const contratoSeleccionadoId = ref(null);

const clausulas = ref([]);
const auditando = ref(false);
const resultadoAuditoria = ref(null);
const reportePDF = ref(null);
const contratoSeleccionadoChat = ref(null);

const chatMensajes = ref([]);
const mensajeActual = ref('');
const enviandoMensaje = ref(false);
const chatHistoryRef = ref(null);


const cerrarSesion = () => {
  authStore.logout();
  router.push('/login');
};

const cargarContratos = async () => {
  cargandoContratos.value = true;
  try {
    const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/v1/contratos/`, {
      headers: { 'Authorization': `Bearer ${authStore.token}` }
    });
    contratos.value = response.data;
  } catch (err) {
    console.error("Error al obtener contratos:", err);
  } finally {
    cargandoContratos.value = false;
  }
};


const abrirBuscador = () => {
  inputBusquedaId.value = '';
  errorBusqueda.value = '';
  contratoVisualizado.value = null;
  mostrarModalBuscador.value = true;
};

const ejecutarBusqueda = () => {
  if (!inputBusquedaId.value) return;
  
  const idABuscar = parseInt(inputBusquedaId.value);
  const contratoEncontrado = contratos.value.find(c => c.id === idABuscar);
  
  if (contratoEncontrado) {
    errorBusqueda.value = '';
    contratoVisualizado.value = contratoEncontrado;
  } else {
    contratoVisualizado.value = null;
    errorBusqueda.value = `No se encontró ningún contrato con el ID #${idABuscar} en tu base de datos.`;
  }
};


const seleccionarArchivo = (event) => {
  const archivo = event.target.files[0];
  archivoSeleccionado.value = archivo;
  
  if (archivo && !tituloContrato.value) {
    tituloContrato.value = archivo.name.replace(/\.[^/.]+$/, "");
  }
  mensaje.value = '';
};

const subirContrato = async () => {
  if (!archivoSeleccionado.value || !tituloContrato.value) return;
  subiendo.value = true;
  mensaje.value = '';
  error.value = false;

  const formData = new FormData();
  formData.append('titulo', tituloContrato.value);
  formData.append('file', archivoSeleccionado.value);

  try {
    await axios.post(`${import.meta.env.VITE_API_URL}/api/v1/contratos/upload`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': `Bearer ${authStore.token}`
      }
    });

    mensaje.value = '¡Contrato subido y registrado con éxito!';
    archivoSeleccionado.value = null;
    tituloContrato.value = '';
    
    await cargarContratos();
    setTimeout(() => {
      vistaActual.value = 'gestion';
      mensaje.value = '';
    }, 1500);

  } catch (err) {
    console.error("Error al subir el contrato:", err);
    error.value = true;
    mensaje.value = 'Error al subir el archivo al servidor.';
  } finally {
    subiendo.value = false;
  }
};


const procesarContrato = async (id) => {
  try {
    contratoSeleccionadoId.value = id;
    const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/v1/contratos/${id}/segmentar`, {}, {
      headers: { 'Authorization': `Bearer ${authStore.token}` }
    });
    clausulas.value = response.data;
    await cargarContratos();
    
    alert("¡Éxito! El contrato ha sido segmentado en cláusulas y guardado en la base de datos.");
    
  } catch (err) {
    console.error("Error en segmentación:", err);
    alert('Error al segmentar el contrato. Verifique que el archivo PDF contenga texto estructurado.');
  }
};

const auditarContrato = async (id) => {
  auditando.value = true;
  contratoSeleccionadoId.value = id;
  resultadoAuditoria.value = null;

  try {
      await axios.post(`${import.meta.env.VITE_API_URL}/api/v1/auditorias/${id}/analizar`, {}, {
        headers: { 'Authorization': `Bearer ${authStore.token}` }
      });

    const intervalo = setInterval(async () => {
      try {
        const res = await axios.get(`${import.meta.env.VITE_API_URL}/api/v1/auditorias/contrato/${id}`, {
          headers: { 'Authorization': `Bearer ${authStore.token}` }
        });

        if (res.data.estado && res.data.estado.toUpperCase().includes('COMPLETAD')) {
            clearInterval(intervalo);
            resultadoAuditoria.value = res.data; 
            auditando.value = false;
            cargarContratos();
        }
        else if (res.data.estado && res.data.estado.toLowerCase() === 'error') {
          clearInterval(intervalo);
          alert('Hubo un error al auditar el contrato con la IA.');
          auditando.value = false;
        }
        
      } catch (err) {
        if (err.response && err.response.status !== 404) {
          console.error("Error al consultar el estado de la auditoría:", err);
        }
      }
    }, 3000); 

  } catch (error) {
    console.error("Error al iniciar la auditoría:", error);
    alert('No se pudo iniciar la auditoría.');
    auditando.value = false;
  }
};


const seleccionarContratoChat = async (item) => {
  const id = item.id ? item.id : item;
  
  contratoSeleccionadoChat.value = item;
  contratoSeleccionadoId.value = id; 
  chatMensajes.value = [];
  
  try {
    const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/v1/contratos/${id}/chat/historial`, {
      headers: { 'Authorization': `Bearer ${authStore.token}` }
    });
    
    if (response.data.mensajes) {
        chatMensajes.value = response.data.mensajes.map(msg => ({
            rol: msg.rol_emisor === 'ia' ? 'ia' : 'user',
            texto: msg.contenido
        }));
    }
  } catch (error) {
    console.error("Error al cargar historial del chat:", error);
  }
};

const scrollChatAbajo = () => {
  nextTick(() => {
    if (chatHistoryRef.value) {
      chatHistoryRef.value.scrollTop = chatHistoryRef.value.scrollHeight;
    }
  });
};

const enviarMensajeChat = async () => {
  if (!mensajeActual.value.trim() || enviandoMensaje.value || !contratoSeleccionadoId.value) return;

  const pregunta = mensajeActual.value.trim();
  chatMensajes.value.push({ rol: 'user', texto: pregunta });
  mensajeActual.value = '';
  enviandoMensaje.value = true;
  scrollChatAbajo();

  try {
   const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/v1/contratos/${contratoSeleccionadoId.value}/chat`, 
      { pregunta: pregunta }, 
      { headers: { 'Authorization': `Bearer ${authStore.token}` } }
    );
    
    const nombreContrato = contratoSeleccionadoChat.value?.nombre_archivo || 'Documento';
    const referencias = (response.data.clausulas_citadas || []).map(cita => `${nombreContrato} - ${cita}`);

    chatMensajes.value.push({ 
        rol: 'ia', 
        texto: response.data.respuesta,
        citas: referencias
    });
  } catch (err) {
    console.error("Error en el chat:", err);
    chatMensajes.value.push({ 
      rol: 'ia', 
      texto: "❌ Ocurrió un error al procesar tu consulta con el asistente de IA." 
    });
  } finally {
    enviandoMensaje.value = false;
    scrollChatAbajo();
  }
};


const descargarPDF = () => {
  const opciones = {
    margin:       0.5,
    filename:     `Reporte_Auditoria_${contratoSeleccionadoId.value}.pdf`,
    image:        { type: 'jpeg', quality: 0.98 },
    html2canvas:  { scale: 2, useCORS: true },
    jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
  };
  
  const btn = document.querySelector('.download-btn');
  if(btn) btn.style.display = 'none';

  html2pdf().set(opciones).from(reportePDF.value).save().then(() => {
    if(btn) btn.style.display = 'flex';
  });
};


const descargarPdfSeguro = async (contratoId) => {
  try {
    const response = await axios.get(`${import.meta.env.VITE_API_URL}/api/v1/auditorias/contrato/${contratoId}/exportar-pdf`, {
      headers: { 'Authorization': `Bearer ${authStore.token}` },
      responseType: 'blob',
    });
    
    const blob = new Blob([response.data], { type: 'application/pdf' });
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = `Reporte_Auditoria_Contrato_${contratoId}.pdf`;
    link.click();
  } catch (err) {
    console.error("Error al descargar el PDF:", err);
    alert('No se pudo descargar el reporte PDF.');
  }
};

const obtenerClaseBadgeRiesgo = (nivel) => {
  if (nivel === 'Alto') return 'riesgo-alto';
  if (nivel === 'Medio') return 'riesgo-medio';
  return 'riesgo-bajo';
};

const obtenerClaseRiesgoGlobal = (puntaje) => {
  if (puntaje >= 70) return 'score-alto';
  if (puntaje >= 30) return 'score-medio';
  return 'score-bajo';
};

onMounted(() => {
  cargarContratos();
  cargarPerfil();
});
</script>

<style scoped>
.dashboard-layout {
  min-height: 100vh;
  background-color: #f1f5f9;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  color: #0f172a;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  color: white;
  padding: 1rem 2.5rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-shield {
  width: 36px;
  height: 36px;
  color: #60a5fa;
}

.brand-titles h1 {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: -0.025em;
}

.brand-company {
  font-size: 0.8rem;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.nav-controls {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.nav-action-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: transparent;
  border: none;
  color: white;
  cursor: pointer;
  transition: opacity 0.2s;
}
.nav-action-btn:hover { opacity: 0.8; }
.nav-text { font-size: 0.9rem; font-weight: 600; }

.profile-avatar {
  background-color: #3b82f6;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.profile-avatar svg { width: 20px; height: 20px; }

.logout-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background-color: rgba(239, 68, 68, 0.15);
  color: #fca5a5;
  border: 1px solid rgba(239, 68, 68, 0.3);
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.2s ease;
}
.logout-btn:hover { background-color: #ef4444; color: white; }
.btn-icon { width: 18px; height: 18px; }

.main-content {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

.welcome-banner { margin-bottom: 2rem; }
.welcome-banner h2 { font-size: 1.875rem; font-weight: 800; color: #0f172a; margin-bottom: 0.25rem; }
.welcome-banner p { color: #64748b; font-size: 1rem; }

.tabs-container {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 1rem;
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: transparent;
  border: none;
  font-size: 1.05rem;
  font-weight: 600;
  color: #64748b;
  padding: 0.5rem 1rem;
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.2s;
}
.tab-btn svg { width: 20px; height: 20px; }
.tab-btn:hover { background-color: #f8fafc; color: #334155; }
.tab-btn.active { color: #2563eb; background-color: #eff6ff; border: 1px solid #bfdbfe; }

.chat-layout {
  display: flex;
  gap: 1.5rem;
  height: calc(100vh - 280px); 
  min-height: 500px;
}

.chat-sidebar {
  width: 300px;
  background: white;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
}

.sidebar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  color: #64748b;
}
.sidebar-title { font-size: 0.85rem; font-weight: 700; text-transform: uppercase; }
.filter-icon { width: 18px; height: 18px; cursor: pointer; }

.chat-list {
  list-style: none;
  padding: 0;
  margin: 0;
  overflow-y: auto;
  flex-grow: 1;
}

.chat-list-empty {
  font-size: 0.9rem;
  color: #94a3b8;
  text-align: center;
  padding: 2rem 0;
}

.chat-list-item {
  padding: 0.85rem 1rem;
  margin-bottom: 0.4rem;
  border-radius: 9999px; 
  cursor: pointer;
  color: #1e293b;
  font-size: 0.95rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: all 0.2s;
}
.chat-list-item:hover { background-color: #f8fafc; }
.chat-list-item.active { background-color: #f1f5f9; font-weight: 600; }

.chat-main {
  flex-grow: 1;
  background: white;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chat-placeholder {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #94a3b8;
  text-align: center;
  padding: 2rem;
}
.chat-placeholder-icon { width: 64px; height: 64px; margin-bottom: 1rem; color: #cbd5e1; }
.chat-placeholder h3 { color: #475569; font-size: 1.25rem; margin-bottom: 0.5rem; }

.chat-active-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.chat-header {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  background-color: #f8fafc;
}
.chat-header h3 { margin: 0; font-size: 1rem; color: #1e293b; }

.chat-history-area {
  flex-grow: 1;
  padding: 1.5rem;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.chat-bubble-wrapper {
  display: flex;
  width: 100%;
}
.chat-bubble-wrapper.user { justify-content: flex-end; }
.chat-bubble-wrapper.ia { justify-content: flex-start; }

.chat-bubble {
  max-width: 75%;
  padding: 1rem 1.25rem;
  border-radius: 12px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}
.chat-bubble-wrapper.user .chat-bubble { background-color: #2563eb; color: white; border-bottom-right-radius: 4px; }
.chat-bubble-wrapper.ia .chat-bubble { background-color: white; color: #1e293b; border: 1px solid #e2e8f0; border-bottom-left-radius: 4px; }

.bubble-author { display: block; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 0.4rem; opacity: 0.8; }
.chat-bubble p { margin: 0; font-size: 0.95rem; white-space: pre-wrap; line-height: 1.6; }

.chat-citations { margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid rgba(0, 0, 0, 0.08); }
.chat-bubble-wrapper.ia .chat-citations { border-top-color: #e2e8f0; }
.citations-title { display: block; font-size: 0.75rem; font-weight: 700; color: #64748b; text-transform: uppercase; margin-bottom: 0.5rem; }
.chat-citations ul { margin: 0; padding: 0; list-style: none; display: flex; flex-direction: column; gap: 0.35rem; }
.chat-citations li { font-size: 0.85rem; color: #475569; background-color: #f1f5f9; padding: 0.4rem 0.75rem; border-radius: 6px; border-left: 3px solid #3b82f6; display: inline-block; word-break: break-word; }

.chat-input-area {
  padding: 1rem 1.5rem;
  background-color: white;
  border-top: 1px solid #e2e8f0;
  display: flex;
  gap: 0.75rem;
}
.chat-input-field { flex-grow: 1; }
.chat-send-btn { display: flex; align-items: center; justify-content: center; padding: 0.75rem 1rem; }
.send-icon { width: 20px; height: 20px; }

.fixed-modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background-color: rgba(15, 23, 42, 0.7);
  backdrop-filter: blur(4px);
  z-index: 50;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: white;
  border-radius: 12px;
  width: 90%;
  max-width: 500px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  animation: modalFadeIn 0.3s ease;
}

@keyframes modalFadeIn {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid #e2e8f0;
  background-color: #f8fafc;
}

.modal-header h3 { margin: 0; font-size: 1.25rem; color: #1e293b; font-weight: 700; }
.close-modal-btn { background: transparent; border: none; font-size: 1.5rem; font-weight: bold; color: #94a3b8; cursor: pointer; line-height: 1; }
.close-modal-btn:hover { color: #ef4444; }
.modal-body { padding: 1.5rem; }

.profile-info-grid, .contract-details-grid { display: flex; flex-direction: column; gap: 1.25rem; }
.info-item, .detail-row { display: flex; flex-direction: column; gap: 0.25rem; }
.detail-row { padding-bottom: 0.75rem; border-bottom: 1px solid #f1f5f9; }
.detail-row:last-child { border-bottom: none; }
.info-label, .detail-row strong { font-size: 0.85rem; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em; font-weight: 700; }
.code-path { font-family: monospace; background-color: #f1f5f9; padding: 0.3rem 0.5rem; border-radius: 4px; font-size: 0.85rem; color: #334155; word-break: break-all; }

.card { background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02); margin-bottom: 1.75rem; border: 1px solid #e2e8f0; }
.card-title-area { display: flex; align-items: center; gap: 1rem; margin-bottom: 1.5rem; }
.card-title-area h3 { margin: 0; font-size: 1.25rem; font-weight: 700; color: #1e293b; }
.card-title-area p { margin: 0.2rem 0 0 0; font-size: 0.875rem; color: #64748b; }
.card-icon { width: 44px; height: 44px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.card-icon svg { width: 24px; height: 24px; }
.card-icon.blue { background-color: #eff6ff; color: #2563eb; }
.card-icon.slate { background-color: #f1f5f9; color: #475569; }
.card-icon.green { background-color: #f0fdf4; color: #16a34a; }
.card-icon.purple { background-color: #faf5ff; color: #9333ea; }

.upload-form { display: flex; flex-direction: column; gap: 1.25rem; }
.input-group { display: flex; flex-direction: column; gap: 0.5rem; }
.input-group label { font-size: 0.875rem; font-weight: 600; color: #334155; }
.text-input { border: 1.5px solid #cbd5e1; padding: 0.75rem 1rem; border-radius: 10px; font-size: 0.95rem; width: 100%; background-color: #f8fafc; }
.text-input:focus { outline: none; border-color: #2563eb; background-color: white; box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1); }
.upload-controls { display: flex; gap: 1rem; align-items: center; }
.file-drop-zone { flex-grow: 1; position: relative; background-color: #f8fafc; border: 1.5px dashed #cbd5e1; border-radius: 10px; }
.file-input { position: absolute; width: 100%; height: 100%; opacity: 0; cursor: pointer; }
.file-label { display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 1rem; }
.file-name-display { font-size: 0.9rem; color: #475569; }
.browse-badge { background-color: #e2e8f0; color: #334155; padding: 0.35rem 0.75rem; border-radius: 6px; font-size: 0.8rem; font-weight: 600; }
.upload-btn { display: flex; align-items: center; justify-content: center; gap: 0.5rem; background-color: #2563eb; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 10px; cursor: pointer; font-weight: 600; font-size: 0.95rem; }
.upload-btn:hover:not(:disabled) { background-color: #1d4ed8; }
.upload-btn:disabled { background-color: #93c5fd; cursor: not-allowed; }

.table-responsive { overflow-x: auto; }
.contracts-table { width: 100%; border-collapse: collapse; margin-top: 0.5rem; }
.contracts-table th, .contracts-table td { padding: 1rem; text-align: left; border-bottom: 1px solid #f1f5f9; }
.contracts-table th { background-color: #f8fafc; color: #475569; font-size: 0.75rem; text-transform: uppercase; font-weight: 700; }
.contracts-table tr:hover { background-color: #f8fafc; }
.id-tag { font-family: monospace; font-weight: 600; color: #64748b; background-color: #f1f5f9; padding: 0.2rem 0.4rem; border-radius: 4px; }
.file-cell { color: #64748b; font-size: 0.9rem; }
.action-buttons-cell { display: flex; gap: 0.5rem; justify-content: flex-end; align-items: center; }
.action-btn { border: none; padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer; font-size: 0.85rem; color: white; font-weight: 600; transition: opacity 0.2s ease; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; }
.action-btn:hover { opacity: 0.9; }
.segment-btn { background-color: #059669; }
.audit-btn { background-color: #7c3aed; }
.audit-btn:disabled { background-color: #c4b5fd; cursor: not-allowed; }
.download-btn-table { background-color: #2b6cb0; padding: 0.5rem 0.75rem; font-size: 0.8rem; }

.badge { display: inline-block; padding: 0.3rem 0.75rem; border-radius: 6px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }
.badge.pendiente { background-color: #fffbeb; color: #b45309; border: 1px solid #fde68a; }
.badge.procesando, .badge.auditado, .badge.auditoria_completada { background-color: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; }
.badge.riesgo-alto { background-color: #fef2f2; color: #dc2626; border: 1px solid #fecaca; }
.badge.riesgo-medio { background-color: #fffbeb; color: #d97706; border: 1px solid #fde68a; }
.badge.riesgo-bajo { background-color: #f0fdf4; color: #16a34a; border: 1px solid #bbf7d0; }

.audit-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem; }
.header-actions { display: flex; gap: 1rem; align-items: center; }
.download-btn { background-color: #2563eb; display: flex; align-items: center; gap: 0.5rem; }
.risk-score-badge { padding: 0.5rem 1rem; border-radius: 8px; font-weight: 700; font-size: 0.9rem; }
.score-alto { background-color: #fef2f2; color: #dc2626; }
.score-medio { background-color: #fffbeb; color: #d97706; }
.score-bajo { background-color: #f0fdf4; color: #16a34a; }
.executive-summary { background-color: #f8fafc; padding: 1.25rem; border-radius: 10px; margin-bottom: 1.5rem; border: 1px solid #e2e8f0; color: #334155; line-height: 1.6; }
.section-subtitle { font-size: 1.1rem; font-weight: 700; color: #1e293b; margin-bottom: 1rem; }
.findings-list, .clauses-list { display: flex; flex-direction: column; gap: 1rem; }
.finding-card, .clause-card { background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 1.25rem; border-radius: 10px; }
.finding-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; }
.finding-clause { font-weight: 700; color: #1e293b; }
.finding-desc, .finding-sug { margin: 0.4rem 0; font-size: 0.95rem; color: #475569; line-height: 1.5; }
.clauses-list { max-height: 450px; overflow-y: auto; padding-right: 0.5rem; }
.clause-card h4 { margin: 0 0 0.5rem 0; color: #1e293b; font-weight: 700; }
.clause-card p { margin: 0; color: #475569; font-size: 0.95rem; line-height: 1.6; white-space: pre-line; }

.empty-state { display: flex; flex-direction: column; align-items: center; gap: 0.75rem; color: #64748b; padding: 2.5rem; text-align: center; }
.alert-message { margin-top: 1rem; padding: 0.75rem 1rem; border-radius: 8px; font-size: 0.875rem; font-weight: 500; }
.alert-message.success { background-color: #f0fdf4; color: #15803d; border: 1px solid #bbf7d0; }
.alert-message.error { background-color: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; }

.typing-indicator { display: flex; gap: 4px; padding: 0.5rem 0; }
.typing-indicator span { width: 8px; height: 8px; background-color: #94a3b8; border-radius: 50%; animation: bounce 1.4s infinite ease-in-out both; }
.typing-indicator span:nth-child(1) { animation-delay: -0.32s; }
.typing-indicator span:nth-child(2) { animation-delay: -0.16s; }
@keyframes bounce { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1.0); } }
.spinner { width: 18px; height: 18px; border: 2px solid rgba(255, 255, 255, 0.3); border-top-color: white; border-radius: 50%; animation: spin 0.8s linear infinite; }
.spinner.dark { border: 2px solid rgba(37, 99, 235, 0.2); border-top-color: #2563eb; }
@keyframes spin { to { transform: rotate(360deg); } }
</style>