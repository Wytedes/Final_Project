<template>
<div>
  <h1>你所热爱的就是你的生活</h1>
  <router-view></router-view>
</div>
</template>

<script>
export default {
    name: 'Msg_One',
    mounted() {
      console.log(this)
    },
}
</script>

<style>

</style>