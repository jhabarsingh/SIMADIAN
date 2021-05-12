<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <Register />
    </template>
  </Drawer>
</template>

<script>
  import Register from '../components/Register'
  import Drawer from '../components/Drawer.vue'
  export default {

    components: {
      Register,
      Drawer
    },
  }
</script>
