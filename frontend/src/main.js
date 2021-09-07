import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

import axios from 'axios'
Vue.prototype.$axios = axios // 全局注册，使用方法为:this.$axios

Vue.config.productionTip = false

// 全局注册组件
import TopBar from '@/components/TopBar.vue'
import SideBar from '@/components/SideBar.vue'
import LinkBar from '@/components/LinkBar.vue'
Vue.component('top-bar', TopBar)
Vue.component('side-bar', SideBar)
Vue.component('link-bar', LinkBar)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
