<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <UserUpdate />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import UserUpdate from '../components/UserUpdate.vue'
  export default {

    components: {
      Drawer,
      UserUpdate
    },
  }
</script>
