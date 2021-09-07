import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
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
    path: '/results',
    name: 'results',
    component: () => import('@/views/Results.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
