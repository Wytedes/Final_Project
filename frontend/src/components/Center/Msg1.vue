<template>
  <div>
    <Movie
    :title="movie_list[0]['title']"
    :oth_title="movie_list[0]['oth_title']"
    :category="movie_list[0]['category']"
    :picture="movie_list[0]['picture']"
    :rating_num="movie_list[0]['rating_num']"
    >
    </Movie>
  </div>
</template>

<script>
import Movie from "./Movie.vue";
export default {
  name: "Msg_One",

  data() {
    return {
      movie_list: [{
        title:'',
        oth_title:'',
        category:'',
        picture:'',
        rating_num:0,
      }],
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
        console.log("执行完成");
      });
  },
};
</script>

<style>
</style>