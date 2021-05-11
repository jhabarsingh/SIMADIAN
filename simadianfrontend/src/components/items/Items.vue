<template>
  <v-container class="grey lighten-5">
    <v-row no-gutters>
      <v-col
        v-for="n in 12"
        :key="n"
        cols="12"
        sm="6"
        style="padding:5px;"
      >
          <Card />
       </v-col>
    </v-row>
    <Pagination />
  </v-container>
</template>

<script>
import Card from './Card.vue'
import Pagination from './Pagination.vue'
export default {
    components: {
        Card,
        Pagination
    },
    data: () => ({
        
    }),
}

</script>
