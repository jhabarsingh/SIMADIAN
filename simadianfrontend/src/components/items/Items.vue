<template>
  <div>
    <v-container class="grey lighten-5"
      v-if="false"
    >
      <search-bar />
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
    
    <div v-else>
      <no-data />
    </div>
    
  </div>
</template>

<script>
import Card from './Card.vue'
import Pagination from './Pagination.vue'
import SearchBar from '../SearchBar.vue';
import NoData from '../NoData.vue'
export default {
    components: {
        Card,
        Pagination,
        SearchBar,
        NoData
    },
    data: () => ({
        
    }),
}

</script>
