<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Top :indexlist="list"/>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Top from './components/Top/Top.vue'

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
    }
  },
  
  components: {
    Top
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
