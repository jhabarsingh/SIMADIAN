<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <UploadItems />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import UploadItems from '../components/items/UploadItems.vue'
  export default {

    components: {
      Drawer,
      UploadItems,
    },
  }
</script>
