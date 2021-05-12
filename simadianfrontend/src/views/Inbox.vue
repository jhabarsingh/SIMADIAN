<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <Received />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import Received from '../components/items/Received.vue'
  export default {

    components: {
      Drawer,
      Received
    },
  }
</script>
