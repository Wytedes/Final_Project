<template>
  <h1>柠檬什么时候酸？</h1>
</template>

<script>
export default {
    name: 'Msg_Two',
    data() {
      return {
        categories: []
      }
    },
    mounted() {
      this.$http
      .get('/api/polls/movie/categories/')
      .then((response)=>{
        console.log(response.data)
      })
      .catch(function (error) {
        console.log('Get Categories Fail!')
      })
    },
}
</script>

<style>

</style>