<template>
  <div id="top">
        <ul>
            <li v-for="item in indexlist" :key='item.title'>
                <a :href="item.link">{{ item.title }}</a>
            </li>
        </ul>
   </div>
</template>

<script>
export default {
    name: 'TopBar',
    props:{
        indexlist: Array,
        expand: Boolean
    },
    data() {
        return {
            flag: this.expand,
        }
    },
    methods: {
        expandIndex () {
            var li1 = document.querySelectorAll("#top ul li:nth-child(1)");
            if(li1.length>0){
                li1[0].style.width = this.flag ? "200px":"100px";
            }
            this.flag = !this.flag
        }
    },
    watch:{
        flag(value, newvalue) {
            this.$emit('expand', newvalue);
        },
    },
    mounted() {
        this.expandIndex();
        var li1 = document.querySelectorAll("#top ul li:nth-child(1)");
        if(li1.length>0){
            li1[0].onclick = this.expandIndex
        }
    },
}

</script>

<style>
    #top {
        flex: 0 0 70px;
        /* height: 70px; */
        background: rgb(0, 225, 255);
        min-width: 1000px;
    }

    #top ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: rgb(84, 114, 153);

        height:100%;
    }

    #top li {
        float: left;
        display: flex;
        flex-flow:column nowrap;
        justify-content: center;    /*主轴内对齐*/
        align-items: stretch;    /*交叉轴对齐*/
        width: 100px;
        height:100%;
    }

    #top li a {
        display: flex;
        flex: 1 0 auto;
        color: white;
        /* padding: 14px; */
        text-decoration: none;
        flex-flow: row nowrap;
        justify-content: center;    /*主轴内对齐*/
        align-items: center;    /*交叉轴对齐*/
    }

    #top ul li:nth-child(1) a{
        border-right: 3px dashed rgb(12, 100, 216);
        margin: 4px;
        margin-left: 0px;
    }

    #top li a:hover {
        background-color: rgb(28, 111, 219);
    }
</style>