<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <Favourite />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import Favourite from '../components/items/Favourite.vue'
  export default {

    components: {
      Drawer,
      Favourite
    },
  }
</script>
