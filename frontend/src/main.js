import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import store from '@/store'

import router from './router'
//应用插件
Vue.use(VueRouter)

import axios from 'axios'
Vue.prototype.$http = axios

// import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css'
//分别引入eleme组件
import { Menu,MenuItem,Submenu  } from 'element-ui';
//应用eleme组件
Vue.component(Menu.name, Menu)
Vue.component(MenuItem.name, MenuItem)
Vue.component(Submenu.name, Submenu)

//关闭生产提示
Vue.config.productionTip = false



new Vue({ 
  render: h => h(App),
  router,
  store,
  }).$mount('#app')

