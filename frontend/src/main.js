import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import store from '@/store'
import axios from 'axios'
Vue.prototype.$http = axios
//关闭生产提示
Vue.config.productionTip = false

//应用插件
Vue.use(VueRouter)

new Vue({ 
  render: h => h(App),
  router,
  store,
  }).$mount('#app')

