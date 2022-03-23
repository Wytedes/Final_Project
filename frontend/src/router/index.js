//该文件用于创建整个应用的路由器
import VueRouter from 'vue-router'
import Msg1 from '../components/Center/Msg1'
import Msg2 from '../components/Center/Msg2'
import Login from '@/components/login'
import HomePage from '@/components/HomePage'

export default new VueRouter({
    routes:[
        {
            path: '/',
            component: HomePage,
            children:[
                
                {
                    path: 'Msg1',
                    component: Msg1,
                    /* children:[
                        { }
                    ] */
                },
                {
                    path: 'Msg2',
                    component: Msg2,
                    
                },
            ]
        },

        {
            path: '/login',
            component: Login,
        },
    ],
})

