<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <MyFiles />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import MyFiles from '../components/user/MyFiles.vue'
  export default {

    components: {
      Drawer,
      MyFiles
    },
  }
</script>
