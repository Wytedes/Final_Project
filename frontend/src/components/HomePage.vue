<template>
    <div id="homepage">
        <Top :indexlist="toplist" :expand="isexpand" @expand='expand'/>
        <Center :indexlist="sidelist" :expand="isexpand"/>
        <Footer/>
    </div>
</template>

<script>
import Top from '@/components/Top/Top.vue';
import Center from '@/components/Center/Center.vue';
import Footer from '@/components/Footer/Footer.vue';
export default {
    name:'HomePage',
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
    #homepage {
    display: flex;
    flex-flow: column nowrap;
    min-height: 100vh;
    background: rgb(255, 255, 255);
    padding: 0;
    margin: 0;
}
</style>