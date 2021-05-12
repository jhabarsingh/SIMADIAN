<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <Items />
    </template>
  </Drawer>
</template>

<script>
  import HomeLogin from '../components/HomeLogin'
  import Drawer from '../components/Drawer.vue'
  import Items from '../components/items/Items.vue'
  export default {

    components: {
      HomeLogin,
      Drawer,
      Items
    },
  }
</script>
