<template>
    <div id='movie'>
        <img :src="picture"/><br>
        <span>{{title}}</span><br>
        <span>{{oth_title}}</span><br>
        <span>{{category}}</span><br>
        <span>{{rating_num}}</span>
    </div>
</template>

<script>
export default {
    name: 'Movie',
    props: [
        'title',
        'oth_title',
        'category',
        'rating_num',
        'picture',
    ],

}
</script>

<style>

</style>