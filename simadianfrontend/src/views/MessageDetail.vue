<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <MessageDetail />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import MessageDetail from '../components/items/MessageDetail.vue'
  export default {

    components: {
      Drawer,
      MessageDetail
    },
  }
</script>
