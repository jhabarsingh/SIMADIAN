<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <Logout />
    </template>
  </Drawer>
</template>

<script>
  import Logout from '../components/Logout'
  import Drawer from '../components/Drawer.vue'
  export default {

    components: {
      Logout,
      Drawer
    },
  }
</script>
