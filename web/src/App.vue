<template>
  <TheHeader />
  <!-- TODO: OnDeck here? -->
  <ListEpisodes :episodes="episodes" />
</template>

<script>
import ListEpisodes from "./components/ListEpisodes.vue";
import TheHeader from "./components/TheHeader.vue";

export default {
  name: "App",
  components: {
    TheHeader,
    ListEpisodes,
  },
  data() {
    return {
      episodes: [],
      showViewed: false,
      serverUrl: "/api",
    };
  },
  provide() {
    return {
      serverUrl: this.serverUrl,
    };
  },
  created() {
    const that = this;
    fetch(this.serverUrl).then(function (response) {
      response.json().then((data) => (that.episodes = data));
    });
  },
};
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
/* If not present, a thin bar appears at top */
* {
  margin: 0;
}

html {
  background-color: black;
  color: yellow;
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  margin: 0 !important;
  padding: 0 !important;
}

body {
  margin: 0 !important;
  padding: 0 !important;
}
</style>
