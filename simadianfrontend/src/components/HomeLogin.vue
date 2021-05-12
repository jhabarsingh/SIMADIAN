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
import Drawer from './Drawer.vue'
import Items from './items/Items.vue'
export default {
  components: {
    Drawer,
    Items,
  }
}
</script>
