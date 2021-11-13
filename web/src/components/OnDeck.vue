<template>
  <div id="on-deck">
    <h2>On Deck</h2>
    <span v-if="episode_id">
      <h3>{{ episode_id }}</h3>
      <h3>{{ name }}</h3>
      <p>Display episode synopsis here.</p>
      <base-button @click="$emit('markViewed', episode_id)"
        >Mark as viewed</base-button
      >
    </span>
    <p v-else>No episode on deck.</p>
  </div>
</template>

<script>
import BaseButton from "./UI/BaseButton.vue";

export default {
  components: {
    BaseButton,
  },
  props: ["episode_id", "name", "viewed"],
  emits: ["markViewed"],
};
</script>

<style scoped>
#on-deck {
  width: 50%;
  margin: 50px auto 50px auto;
}
</style>