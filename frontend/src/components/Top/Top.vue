<template>
  <!-- 
  <div id="top">
        <a id="indexa" href="#Msg1">目录</a>
        <ul>
            <li v-for="item in indexlist" :key='item.title'>
                <a class="item" :href="item.link">{{ item.title }}</a>
            </li>
        </ul>
   </div>
    -->
    <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
    >
        <el-menu-item v-for="(category, index) in categories" :key="index" :index="(index+1).toString()">{{category[0]}}</el-menu-item>
        <el-submenu index="worktable">
            <template slot="title">我的工作台</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
            <el-menu-item index="2-3">选项3</el-menu-item>
            <el-submenu index="2-4">
                <template slot="title">选项4</template>
                <el-menu-item index="2-4-1">选项1</el-menu-item>
                <el-menu-item index="2-4-2">选项2</el-menu-item>
                <el-menu-item index="2-4-3">选项3</el-menu-item>
            </el-submenu>
        </el-submenu>
        <el-menu-item index="msgcen" :disabled="false">消息中心</el-menu-item>
        <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">订单管理</a></el-menu-item>
    </el-menu>
</template>

<script>
export default {
  name: "TopBar",
  props: {
    indexlist: Array,
  },
  data(){
      return {
          activeIndex2: '1',
          categories:[],
      }
  },
  methods: {
    expandIndex() {
      var indexa = document.getElementById("indexa");
      indexa.style.flexBasis = this.expand ? "193px" : "93px";
    },
    handleSelect(key, keyPath) {
        console.log(key, keyPath);
    },
  },
  computed: {
    expand() {
      return this.$store.state.expand;
    },
  },
  mounted() {
/* 
    this.expandIndex();
    var indexa = document.getElementById("indexa");
    indexa.onclick = () => {
      this.$store.commit("expandChange");
      this.expandIndex();
    };
     */
    this.$http
      .get('/api/polls/movie/categories/')
      .then((response)=>{
        this.categories = response.data
      })
      .catch(function (error) {
        console.log('Get Categories Fail!')
      })
  },
};
</script>

<style>
#top {
  flex: 0 0 70px;
  /* height: 70px; */
  background-color: rgb(84, 114, 153);
  min-width: 1000px;

  display: flex;
  flex-flow: row nowrap;
  justify-content: flex-start;
}

#top ul {
  flex: 1 0 70px;
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: rgb(84, 114, 153);

  height: 100%;
}

#top li {
  float: left;
  display: flex;
  flex-flow: column nowrap;
  justify-content: center; /*主轴内对齐*/
  align-items: stretch; /*交叉轴对齐*/
  width: 100px;
  height: 100%;
}

#top li a.item {
  display: flex;
  flex: 1 0 auto;
  color: white;
  /* padding: 14px; */
  text-decoration: none;
  flex-flow: row nowrap;
  justify-content: center; /*主轴内对齐*/
  align-items: center; /*交叉轴对齐*/
}

#indexa {
  display: flex;
  flex: 0 0 93px;
  border-right: 3px dashed rgb(12, 100, 216);
  margin: 4px;
  margin-left: 0px;
  color: white;
  /* padding: 14px; */
  text-decoration: none;
  flex-flow: row nowrap;
  justify-content: center; /*主轴内对齐*/
  align-items: center; /*交叉轴对齐*/
}
/* 
    #top ul li:nth-child(1) a{
        border-right: 3px dashed rgb(12, 100, 216);
        margin: 4px;
        margin-left: 0px;
    }
 */
#top a:hover,
#indexa:hover {
  background-color: rgb(28, 111, 219);
}

#top #login {
  float: right;
  height: 100%;
}
</style>