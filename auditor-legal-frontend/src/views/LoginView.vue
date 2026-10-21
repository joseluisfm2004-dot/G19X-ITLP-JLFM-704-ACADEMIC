<template>
  <div class="login-wrapper">
    <div class="brand-section">
      <div class="brand-content">
        <div class="logo-badge">
          <svg xmlns="http://www.w3.org/2000/svg" class="shield-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
          </svg>
        </div>
        <h1>Auditor Inteligente de Contratos</h1>
        <p class="brand-subtitle">Sistema Avanzado de Auditoría Legal RAG potenciado por Azure OpenAI & Enterprise Security</p>
        <div class="features-list">
          <div class="feature-item">
            <span class="dot"></span> Análisis automatizado de cláusulas
          </div>
          <div class="feature-item">
            <span class="dot"></span> Validación y auditoría inteligente con IA
          </div>
          <div class="feature-item">
            <span class="dot"></span> Consultas conversacionales precisas
          </div>
        </div>
      </div>
      <div class="brand-footer">
        <span>Tecnológico Nacional de México</span>
      </div>
    </div>

    <div class="form-section">
      <div class="login-card">
        <div class="card-header">
          <h2>Iniciar Sesión</h2>
          <p>Ingrese sus credenciales corporativas para acceder al panel</p>
        </div>
        
        <form @submit.prevent="handleLogin" class="login-form">
          <div class="input-group">
            <label for="email">Correo electrónico</label>
            <div class="input-field-wrapper">
              <span class="input-icon">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon-svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" />
                </svg>
              </span>
              <input 
                id="email" 
                type="email" 
                v-model="email" 
                required 
                placeholder="nombre@empresa.com" 
                autocomplete="email"
              />
            </div>
          </div>
          
          <div class="input-group">
            <label for="password">Contraseña</label>
            <div class="input-field-wrapper">
              <span class="input-icon">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon-svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                </svg>
              </span>
              <input 
                id="password" 
                type="password" 
                v-model="password" 
                required 
                placeholder="••••••••••••" 
                autocomplete="current-password"
              />
            </div>
          </div>
          
          <button type="submit" class="submit-btn" :disabled="isLoading">
            <span v-if="isLoading" class="spinner"></span>
            <span v-if="isLoading">Verificando credenciales...</span>
            <span v-else>Acceder al Sistema</span>
          </button>
          
          <transition name="fade">
            <div v-if="errorMessage" class="error-alert">
              <svg xmlns="http://www.w3.org/2000/svg" class="error-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
              </svg>
              <span>{{ errorMessage }}</span>
            </div>
          </transition>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useAuthStore } from '../stores/auth';

const email = ref('');
const password = ref('');
const isLoading = ref(false);
const errorMessage = ref('');

const router = useRouter();
const authStore = useAuthStore();

const handleLogin = async () => {
  isLoading.value = true;
  errorMessage.value = '';
  
  try {
    const formData = new URLSearchParams();
    formData.append('username', email.value); 
    formData.append('password', password.value);

const response = await axios.post(`${import.meta.env.VITE_API_URL}/api/v1/auth/login`, formData, {      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });

    authStore.setToken(response.data.access_token);
    router.push('/dashboard');
    
  } catch (error) {
    console.error("Error en login:", error);
    errorMessage.value = 'Credenciales inválidas o el servidor no responde.';
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.login-wrapper {
  display: flex;
  min-height: 100vh;
  width: 100vw;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  background-color: #0f172a;
}

.brand-section {
  flex: 1;
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 4rem;
  position: relative;
  overflow: hidden;
  border-right: 1px solid rgba(255, 255, 255, 0.08);
}

.brand-section::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(37, 99, 235, 0.08) 0%, transparent 60%);
  pointer-events: none;
}

.brand-content {
  z-index: 1;
  max-width: 480px;
  margin: auto 0;
}

.logo-badge {
  width: 56px;
  height: 56px;
  background: rgba(37, 99, 235, 0.2);
  border: 1px solid rgba(59, 130, 246, 0.4);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 2rem;
  box-shadow: 0 0 25px rgba(37, 99, 235, 0.3);
}

.shield-icon {
  width: 30px;
  height: 30px;
  color: #60a5fa;
}

.brand-section h1 {
  font-size: 2.75rem;
  font-weight: 800;
  letter-spacing: -0.025em;
  margin-bottom: 1rem;
  color: #f8fafc;
}

.brand-subtitle {
  font-size: 1.125rem;
  color: #94a3b8;
  line-height: 1.6;
  margin-bottom: 2.5rem;
}

.features-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.feature-item {
  display: flex;
  align-items: center;
  font-size: 0.95rem;
  color: #cbd5e1;
  font-weight: 500;
}

.dot {
  width: 8px;
  height: 8px;
  background-color: #3b82f6;
  border-radius: 50%;
  margin-right: 12px;
  box-shadow: 0 0 8px #3b82f6;
}

.brand-footer {
  z-index: 1;
  font-size: 0.85rem;
  color: #64748b;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

.form-section {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f8fafc;
  padding: 2rem;
}

.login-card {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
  width: 100%;
  max-width: 440px;
  border: 1px solid #e2e8f0;
}

.card-header {
  margin-bottom: 2rem;
}

.card-header h2 {
  font-size: 1.875rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 0.5rem;
  letter-spacing: -0.02em;
}

.card-header p {
  color: #64748b;
  font-size: 0.95rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.input-group label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #334155;
}

.input-field-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  left: 1rem;
  display: flex;
  align-items: center;
  pointer-events: none;
}

.icon-svg {
  width: 20px;
  height: 20px;
  color: #94a3b8;
}

input {
  width: 100%;
  padding: 0.875rem 1rem 0.875rem 2.8rem;
  background-color: #f8fafc;
  border: 1.5px solid #cbd5e1;
  border-radius: 10px;
  font-size: 0.95rem;
  color: #0f172a;
  transition: all 0.2s ease;
}

input:focus {
  outline: none;
  border-color: #2563eb;
  background-color: white;
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.1);
}

.submit-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  width: 100%;
  padding: 0.875rem;
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
  color: white;
  border: none;
  border-radius: 10px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
  margin-top: 0.5rem;
}

.submit-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
  transform: translateY(-1px);
  box-shadow: 0 6px 16px rgba(37, 99, 235, 0.35);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

.spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-alert {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.875rem 1rem;
  background-color: #fef2f2;
  border: 1px solid #fecaca;
  border-radius: 10px;
  color: #b91c1c;
  font-size: 0.875rem;
  font-weight: 500;
}

.error-icon {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}

@media (max-width: 900px) {
  .brand-section {
    display: none;
  }
}
</style>