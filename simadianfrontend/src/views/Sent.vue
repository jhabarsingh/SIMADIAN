<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <Sent />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import Sent from '../components/items/Sent.vue'
  export default {

    components: {
      Drawer,
      Sent
    },
  }
</script>
