<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Top :indexlist="list" :expand="isexpand" @expand='expand'/>
    <Center :indexlist="list" :expand="isexpand" @expand='expand'/>
    <Footer/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Top from './components/Top/Top.vue';
import Center from './components/Center/Center.vue';
import Footer from './components/Footer/Footer.vue';
export default {
  name: 'App',
  data () {
    return {
      list:[
        {title: '目录', link: '#home'},
        {title: '新闻', link: '#news'},
        {title: '联系', link: '#contact'},
        {title: '关于', link: '#about'},
      ],
      flag: -1,
      isexpand: false,
    }
  },
  components: {
    Top,
    Center,
    Footer,
  },
  methods: {
    expand(flag){
      this.isexpand = flag;
    }
  },
}
</script>

<style>
#app {
    display: flex;
    flex-flow: column nowrap;
    min-height: 100vh;
    background: rgb(255, 255, 0);
    padding: 0;
    margin: 0;
}
</style>
