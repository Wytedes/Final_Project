<template>
    <div id="center">
        <SideBar :indexlist="indexlist" :expand="expand"></SideBar>
        <div id="content">
            <!-- 指定组件的呈现位置 -->
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import SideBar from './SideBar.vue'
export default {
    name: "CenterContent",
    props:{
        indexlist: Array,
        expand: Boolean
    },
    components:{
        SideBar,
    },
}
</script>

<style>
    #center {
        flex: 1 0 650px;
        background: rgb(255, 255, 255);
        justify-content: space-between;

        display: flex;
        flex-flow: row nowrap;
    }

    #center #content {
        flex: 1 0 500px;
        height: 100%;
        background: rgb(50, 86, 92);
    }

</style>