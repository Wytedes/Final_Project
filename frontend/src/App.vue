<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Top :indexlist="toplist" :expand="isexpand" @expand='expand'/>
    <Center :indexlist="sidelist" :expand="isexpand"/>
    <Footer/>
    <!-- <HelloWorld/> -->
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Top from './components/Top/Top.vue';
import Center from './components/Center/Center.vue';
import Footer from './components/Footer/Footer.vue';
// import Login from '@/components/login.vue';
export default {
  name: 'App',
  data () {
    return {
      toplist:[
        {title: '目录', link: '#home'},
        {title: '新闻', link: '#news'},
        {title: '联系', link: '#contact'},
        {title: '关于', link: '#about'},
      ],
      sidelist:[
        {title: 'Msg1', to: '/Msg1'},
        {title: 'Msg2', to: '/Msg2'},
      ],
      flag: -1,
      isexpand: false,
    }
  },
  components: {
    Top,
    Center,
    Footer,
    // HelloWorld,
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
    background: rgb(255, 255, 255);
    padding: 0;
    margin: 0;
}
</style>
