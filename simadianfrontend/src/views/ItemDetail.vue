<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <ItemDetail />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import ItemDetail from '../components/items/ItemDetail.vue'
  export default {

    components: {
      Drawer,
      ItemDetail
    },
  }
</script>
