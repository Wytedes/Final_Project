<template>
    <div id="index">
        <ul>
            <li v-for="item in indexlist" :key='item.title'>
                <router-link active-class="active" :to="item.to">{{ item.title }}</router-link>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name:'SideBar',
    props: {
        indexlist: Array,
    },
    computed:{
        expand(){
            return this.$store.state.expand;
        }
    },
    watch:{
        expand(){
            this.expandIndex();
        }
    },
    methods: {
        expandIndex () {
            var index = document.getElementById('index');
            index.style.flexBasis = this.expand ? "200px":"100px";
            var indexa = index.querySelectorAll('li a')
            for(var i=0;i<indexa.length;i++){
                indexa[i].style.justifyContent = this.expand ? "flex-end":"flex-start"
            }
        },
    },
    mounted() {
        this.expandIndex();
    },
}
</script>

<style scoped>
    #center #index {
        flex: 0 0 100px;
        height: 100%;
        background: #000;
    }
    #index ul {
        display: flex;
        flex-flow: column nowrap;
        height: 100%;

        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: rgb(156, 165, 175);

    }

    #index li {
        flex: 0 0 75px;
        display:flex;
        flex-flow: row nowrap;
        justify-content: center;    /*主轴内对齐*/
        align-items: stretch;    /*交叉轴对齐*/
    }

    #index li a {
        flex:1 0 auto;
        display: flex;
        color: white;
        padding-left: 14px;
        padding-right: 30px;
        text-decoration: none;

        flex-flow: row nowrap;
        justify-content: flex-start;    /*主轴内对齐*/
        align-items: center;    /*交叉轴对齐*/
        /* align-content: center;  主轴间对齐 */
    }

    #index li a:hover {
        background-color: rgb(78, 121, 177);
    }

    #index li a.active {
        background-color: rgb(28, 111, 219);
    }
</style>