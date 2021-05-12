<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <Login />
    </template>
  </Drawer>
</template>

<script>
  import Login from '../components/Login'
  import Drawer from '../components/Drawer.vue'
  export default {

    components: {
      Login,
      Drawer
    },
  }
</script>
