<template>
  <tr>
    <slot></slot>
  </tr>
</template>

<script>
export default {};
</script>

<style scoped>
tr:nth-child(even) {
  background-color: rgb(30, 30, 30);
}

tr:hover {
  background-color: yellow;
  color: black;
  cursor: pointer;
}
</style>
