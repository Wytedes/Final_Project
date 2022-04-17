<template>
  <ul id="movie">
    <li class="item">
      <div id="imgwrapper"><img :src="picture" /></div>
    </li>
    <li class="item">
      <div class="text">{{ title }}</div>
    </li>
    <li class="item">
      <div class="text">{{ oth_title || "..." }}</div>
    </li>
    <li class="item">
      <div class="text">{{ category }}</div>
    </li>
    <li class="item">
      <div class="text">{{ rating_num }}</div>
    </li>
    <li class="item" v-if="this.$store.state.login_user">
      <el-rate
        v-model="value"
        allow-half
        @change="change_value"
        :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
      >
      </el-rate>
    </li>
  </ul>
</template>

<script>
export default {
  name: "Movie",
  props: ["title", "oth_title", "category", "rating_num", "picture"],

  data() {
    return {
      value: null,
    };
  },

  methods: {
    change_value(newvalue) {
      console.log(newvalue);
      this.$http.get("/api/polls/movie/rate/", {
        params: {
          movie: this.title,
          rate_num: newvalue,
        },
      });
    },
  },

  mounted() {
    if (this.$store.state.login_user) {
      this.$http
        .get("/api/polls/movie/getrate/", {
          params: {
            movie: this.title,
          },
        })
        .then((response) => {
          if (response.status === 200) {
            this.value = response.data.rate_num;
            console.log(this.value)
          }
        });
    }
  },
};
</script>

<style scoped>
#movie {
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;

  width: 150px;
  margin: 0;
  padding: 10px;

  list-style-type: none;
  border: 2px solid rgb(0, 110, 124);
}
.item {
  flex: 0 0 21px;
}
#imgwrapper {
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;

  width: 100%;
  height: 160px;
  overflow: hidden;
  margin-bottom: 3px;
}
img {
  height: 100%;
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