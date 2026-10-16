import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../views/LoginView.vue';
import DashboardView from '../views/DashboardView.vue'; 

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView 
    },
    {
      path: '/',
      redirect: '/login'
    }
  ]
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('token');
  
  if (to.name !== 'login' && !isAuthenticated) {
    next({ name: 'login' }); 
  } else {
    next(); 
  }
});

export default router;