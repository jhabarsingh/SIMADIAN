<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <WriteMessage />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import WriteMessage from '../components/items/WriteMessage.vue'
  export default {

    components: {
      Drawer,
      WriteMessage
    },
  }
</script>
