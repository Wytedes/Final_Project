<template>
  <div id="Content">
    <div id="post" v-for="(movie, index) in movie_list" :key="index">
      <Movie
        :title="movie['title']"
        :oth_title="movie['oth_title']"
        :category="movie['category']"
        :picture="movie['picture']"
        :rating_num="movie['rating_num']"
      >
      </Movie>
    </div>
  </div>
</template>

<script>
import Movie from "./Movie.vue";
export default {
  name: "Msg_One",

  data() {
    return {
      movie_list: [
        {
          title: "",
          oth_title: "",
          category: "",
          picture: "",
          rating_num: undefined,
        },
      ],
    };
  },

  components: {
    Movie,
  },

  mounted() {
    this.$http
      .post(
        "/api/polls/movie/",
        { account: "zhanglin", password: "654321" },
        {
          transformRequest: [
            function (data) {
              // Do whatever you want to transform the data
              let ret = "";
              for (let it in data) {
                ret +=
                  encodeURIComponent(it) +
                  "=" +
                  encodeURIComponent(data[it]) +
                  "&";
              }
              return ret;
            },
          ],
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      )
      .then((response) => {
        this.movie_list = response.data;
        console.log(response.data);
      })
      .catch(function (error) {
        console.log(error);
      })
      .then(function () {
        // 总是会执行
        // console.log("执行完成");
      });
  },
};
</script>

<style>
#Content{
  display:flex;
  flex-flow: row wrap;

  justify-content: space-around;
}
#post{
  display:flex;
  flex:0 0 33%;
}
</style>