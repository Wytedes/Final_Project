<template>
    <div id="login">
        登陆名：
        <input type="text" name="username" />
        <br/>
        密码：
        <input type="password" name="password" />
        <br/>
        <button @click="test">登陆</button>&nbsp;<button>注册</button>
    </div>
</template>

<script>
export default {
    name: 'LoginPage',
    methods: {
        test(){
            this.$router.push('/')
        }
    },
}
</script>

<style>

</style>