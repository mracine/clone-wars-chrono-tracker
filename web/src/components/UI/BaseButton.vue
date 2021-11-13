<template>
  <button>
    <slot></slot>
  </button>
</template>

<style scoped>
button {
  background-color: black;
  border-color: yellow;
  color: yellow;
}

button:hover {
  background-color: yellow;
  color: black;
  cursor: pointer;
}
</style>