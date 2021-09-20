import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/endusers',
    name: 'endusers',
    component: () => import('@/views/Endusers.vue')
  },
  {
    path: '/buildings',
    name: 'buildings',
    component: () => import('@/views/Buildings.vue')
  },
  {
    path: '/gates',
    name: 'gates',
    component: () => import('@/views/Gates.vue')
  },
  {
    path: '/devices',
    name: 'devices',
    component: () => import('@/views/Devices.vue')
  },
  {
    path: '/logs',
    name: 'logs',
    component: () => import('@/views/Logs.vue')
  },
  {
    path: '/status',
    name: 'status',
    component: () => import('@/views/Status.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/result',
    name: 'result',
    component: () => import('@/views/Result.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
