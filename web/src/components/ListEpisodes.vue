<template>
  <!-- onDeck may not be loaded at app startup -->
  <OnDeck
    v-if="onDeck"
    :episode_id="onDeck.episode_id"
    :name="onDeck.name"
    :viewed="onDeck.viewed"
    @markViewed="toggleViewedStatus"
  />
  <div>
    <!-- TODO -->
    <!-- <progress
      id="progress-bar"
      :value="viewedEpisodes.length"
      :max="episodes.length"
    >
      {{ viewedEpisodes.length }} / {{ episodes.length }}
    </progress> -->
  </div>
  <!-- TODO: add into filter options -->
  <div id="table-options">
    <base-checkbox> </base-checkbox>
    <input
      type="checkbox"
      id="show-viewed"
      name="show-viewed"
      v-model="showViewed"
    />
    <label for="show-viewed">Viewed</label>
    <input
      type="checkbox"
      id="show-unviewed"
      name="show-unviewed"
      v-model="showUnviewed"
    />
    <label for="show-unviewed">Unviewed</label>
  </div>
  <div id="backlog">
    <table v-if="displayedEpisodes.length > 0">
      <base-table-row>
        <th></th>
        <th></th>
        <th>Name</th>
        <th></th>
      </base-table-row>
      <!-- TODO: be careful of :=, id also gets bound -->
      <!-- <base-table-row>
        <td :class="viewedStyle">{{ id }}</td>
        <td :class="viewedStyle">{{ episode_id }}</td>
        <td :class="viewedStyle">{{ name }}</td>
        <td :class="viewedStyle">
          <base-button type="button" @click="$emit('viewedClick', episode_id)">
            {{ viewedDisplayText }}
          </base-button>
        </td>
      </base-table-row> -->
      <episode-table-row
        v-for="episode in displayedEpisodes"
        :key="episode.episode_id"
        :id="episode.id"
        :episode_id="episode.episode_id"
        :name="episode.name"
        :viewed="episode.viewed"
        @viewedClick="toggleViewedStatus"
      ></episode-table-row>
    </table>
    <p v-else>No episodes to display.</p>
  </div>
</template>

<script>
import EpisodeTableRow from "./EpisodeTableRow.vue";
import BaseCheckbox from "./UI/BaseCheckbox.vue";
import BaseTableRow from "./UI/BaseTableRow.vue";
import OnDeck from "./OnDeck.vue";

export default {
  components: {
    BaseCheckbox,
    BaseTableRow,
    EpisodeTableRow,
    OnDeck,
  },
  props: ["episodes"],
  data() {
    return {
      showViewed: false,
      showUnviewed: true,
    };
  },
  computed: {
    viewedClassStyle() {
      return 0;
    },
    onDeck() {
      return this.episodes.find((episode) => episode.viewed === false);
    },
    displayedEpisodes() {
      if (this.showViewed && this.showUnviewed) {
        return this.episodes;
      } else if (this.showViewed) {
        return this.viewedEpisodes;
      } else if (this.showUnviewed) {
        return this.unviewedEpisodes;
      } else {
        return [];
      }
    },
    viewedEpisodes() {
      return this.episodes.filter((episode) => episode.viewed != false);
    },
    unviewedEpisodes() {
      return this.episodes.filter((episode) => episode.viewed != true);
    },
  },
  inject: ["serverUrl"],
  methods: {
    toggleViewedStatus(episode_id) {
      const episode = this.episodes.find(
        (episode) => episode_id === episode.episode_id
      );
      episode.viewed = !episode.viewed;

      fetch(this.serverUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          episode_id: episode_id,
          viewed: episode.viewed,
        }),
      });
    },
  },
};
</script>

<style scoped>
/* See https://stackoverflow.com/questions/41429906/how-to-display-data-label-inside-html5-progress-bar-cross-browser for progress bars */
progress {
  width: 25%;
  margin: auto;
}

#table-options {
  width: 50%;
  margin: auto;
}

#backlog {
  width: 50%;
  margin: auto;
}

table {
  /* display: block; for scrolling */
  /* height: 500px; */
  /* overflow: auto; */
  margin: auto;
  margin-bottom: 5rem;
  border-collapse: collapse;
}

table,
th {
  border: 1px solid yellow;
}

th {
  background-color: yellow;
  color: black;
}
</style>