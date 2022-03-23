//该文件用于创建Vuex中最为核心的store

//引入Vuex
import Vue from 'vue'
import Vuex from 'vuex'
//准备actions——用于响应组件中的动作
const actions = {
}

//准备mutation——用于操作数据(state)
const mutations = {
    expandChange(state){
        state.expand = !state.expand
    }
}

//准备state——用于存储数据
const state = {
    expand: false,
}

const getters = {

}
Vue.use(Vuex)
//创建并导出store
export default new Vuex.Store({
    actions,
    mutations,
    state,
    getters,
})