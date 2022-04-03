<template>
    <div id="center">
        <!-- <SideBar :indexlist="indexlist"></SideBar> -->
        <div id="content">
            <!-- 指定组件的呈现位置 -->
            <keep-alive include="Msg1">
                <router-view></router-view>
            </keep-alive>
        </div>
    </div>
</template>

<script>
import SideBar from './SideBar.vue'
export default {
    name: "CenterContent",
    props:{
        indexlist: Array,
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
        background: rgb(129, 129, 129);
    }

</style>