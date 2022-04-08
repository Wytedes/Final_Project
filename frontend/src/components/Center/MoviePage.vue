<template>
  <div id="Content">
    <div id="MovieList">
      <template v-for="m in movie_list">
        <div id="post" v-if="IsShow(m)" :key="m.title">
          <Movie
            :title="m['title']"
            :oth_title="m['oth_title']"
            :category="m['category']"
            :picture="m['picture']"
            :rating_num="m['rating_num']"
          >
          </Movie>
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import Movie from "./Movie.vue";
export default {
  name: "MoviePage",

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

  computed: {
    category() {
      return this.$store.state.category;
    },
  },

  methods: {
    IsShow(movie){
      if(this.category=='全部' || movie.category.includes(this.category)) return true;
      else return false;
    },
  },
/* 
  watch: {
    category(newvalue) {
      this.$http
        .get("/api/polls/movie/", {
          params: {
            category: newvalue,
          },
        })
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
    
  }, */

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
#Content {
  display: flex;
  flex-flow: row nowrap;
}
#MovieList {
  display: flex;
  flex:0 0 40%;
  flex-flow: row wrap;

  justify-content: flex-start;
}
#post {
  display: flex;
  flex: 0 0 25%;
}
</style>