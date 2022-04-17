//该文件用于创建Vuex中最为核心的store

//引入Vuex
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
//准备actions——用于响应组件中的动作
const actions = {
    check_login_status(context) {
        console.log(context)
        axios
            .get(
                "/api/logstatus/"
            )
            .then((res) => {
                if (res.status === 200) {
                    context.commit('refresh_login_status', res.data['user']);
                }
                else {
                    context.commit('refresh_login_status', null);
                }
            });
    }
}

//准备mutation——用于操作数据(state)
const mutations = {
    expandChange(state) {
        state.expand = !state.expand;
    },
    changeCategory(state, category) {
        state.category = category;
    },
    refresh_login_status(state, user){
        state.login_user = user;
    }
}

//准备state——用于存储数据
const state = {
    expand: false,
    category: '全部',
    login_user: null,
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