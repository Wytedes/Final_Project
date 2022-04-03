<template>
    <ul id='movie'>
        <li class="item"><div id="imgwrapper"><img :src="picture"/></div></li>
        <li class="item"><div class="text">{{title}}</div></li>
        <li class="item"><div class="text">{{oth_title}}</div></li>
        <li class="item"><div class="text">{{category}}</div></li>
        <li class="item"><div class="text">{{rating_num}}</div></li>
    </ul>
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

<style scoped>
    #movie {
        display: flex;
        flex-flow: column nowrap;
        justify-content: flex-start;
        
        width:115px;
        margin: 0;
        padding: 0;

        list-style-type: none;
    }
    #imgwrapper {
        width:100%;
        height: 160px;
        overflow: hidden;
        margin-bottom: 3px;
    }
    img {
        height:100%; 
        object-fit: fill;
    }
    .text {
        text-align: left;
        width: 100%;
        /*强制文字在一行文本框内*/
		white-space: nowrap;
		/*溢出部分文字隐藏*/
		overflow: hidden;
		/*溢出部分省略号处理*/
		text-overflow: ellipsis;
    }
</style>