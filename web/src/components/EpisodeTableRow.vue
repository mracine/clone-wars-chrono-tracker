<template>
  <base-table-row>
    <td :class="viewedStyle">{{ id }}</td>
    <td :class="viewedStyle">{{ episode_id }}</td>
    <td :class="viewedStyle">{{ name }}</td>
    <td :class="viewedStyle">
      <base-button type="button" @click="$emit('viewedClick', episode_id)">
        {{ viewedDisplayText }}
      </base-button>
    </td>
  </base-table-row>
</template>

<script>
import BaseTableRow from "./UI/BaseTableRow.vue";

export default {
  components: { BaseTableRow },
  emits: ["viewedClick"],
  props: ["id", "episode_id", "name", "viewed"],
  computed: {
    viewedStyle() {
      var classes = "";
      if (this.viewed) {
        classes += "viewed ";
      }
      return classes;
    },
    viewedDisplayText() {
      return this.viewed === true ? "Mark as unviewed" : "Mark as viewed";
    },
  },
};
</script>

<style scoped>
td {
  border: 1px solid yellow;
  text-align: center;
  padding: 1rem 1rem 1rem 1rem;
}

td.viewed {
  color: gray;
}
</style>