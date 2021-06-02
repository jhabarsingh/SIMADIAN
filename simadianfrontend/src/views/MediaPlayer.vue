<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <VideoPlayer />
    </template>
  </Drawer>
</template>

<script>
  import VideoPlayer from '../components/others/VideoPlayer'
  import Drawer from '../components/Drawer.vue'
  export default {

    components: {
      VideoPlayer,
      Drawer
    },
  }
</script>
