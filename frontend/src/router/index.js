import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import store from "../store";

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
    component: Login,
    meta: {
      requireAuth: false
    }
  },
  {
    path: '/result',
    name: 'result',
    component: () => import('@/views/Result.vue'),
    meta: {
      requireAuth: true
    }
  },
]

const router = new VueRouter({
  routes
})

// 路由守卫
router.beforeEach((to, from, next)=>{
  if (to.matched.some(record => record.meta.requireAuth)) {
    if (to.path === '/login') { // 如果是登录页面的话，直接next() -->解决注销后的循环执行bug
      next();
    } else if (to.path === '/result'){
      if (from.path === '/login') // 否则 仅在login->result时正常执行跳转
        next()
      else
        next({ path: '/login' });
    }
  } else {
    next();
  }
})

export default router
