<template>
  <Drawer
  >
    <template
      v-slot:main
    >
      <SearchFilter />
    </template>
  </Drawer>
</template>

<script>
  import Drawer from '../components/Drawer.vue'
  import SearchFilter from '../components/SearchFilter.vue'
  export default {

    components: {
      Drawer,
      SearchFilter
    },
  }
</script>
