<template>
    <div id="login">
        <h1 @click="test">Hello</h1>
    </div>
</template>

<script>
export default {
    name: 'LoginPage',
    methods: {
        test(){
            this.$router.push('/HelloWorld')
        }
    },
}
</script>

<style>

</style>