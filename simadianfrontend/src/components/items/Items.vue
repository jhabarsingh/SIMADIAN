<template>
  <div>
    <v-container class="grey lighten-5"
      v-if="true"
    >
      <search-bar />
      <v-row no-gutters>
        <v-col
          v-for="(n, i) in items"
          :key="i"
          cols="12"
          sm="6"
          style="padding:5px;"
        >
            <Card 
              :title="n.name" 
              :description="n.description" 
              :thumbnail="[n.thumbnail1, n.thumbnail2]" 
              :category="n.category"
              :writer="n.writer"
              :cost_price="n.cost_price"
              :sell_price="n.sell_price"
            />

        </v-col>
      </v-row>
    </v-container>
    
    <div v-else>
      <no-data />
    </div>
    
      <template>
        <div class="text-center">
          <v-container>
            <v-row justify="center">
              <v-col cols="8">
                <v-container class="max-width">
                  <v-pagination
                    v-model="page"
                    class="my-4"
                    :length="Math.ceil(+count / 10)"
                  ></v-pagination>
                </v-container>
              </v-col>
            </v-row>
          </v-container>
        </div>
      </template>
  </div>
</template>

<script>
import Card from './Card.vue'
import Pagination from './Pagination.vue'
import SearchBar from '../SearchBar.vue';
import NoData from '../NoData.vue'
import axios from 'axios';

export default {
    components: {
        Card,
        SearchBar,
        NoData
    },
    data: () => ({
      count: 1,
      page: 1,  
      items: null
    }),
    watch: {
      'page' (val) {
        this.$router.push({
          name: 'HomeLogin', 
          query: {
            page: val
          }
        })
      }
    },
    methods: {
      
    },
    async created() {
      let item;
      
      if(this.$route.query.page) {
        item = await axios.get(this.$store.state.URL + "items/" + '?page=' + this.$route.query.page)
        this.page = +this.$route.query.page;
      }
      else {
        item = await axios.get(this.$store.state.URL + "items/")      
      }
      this.items = (item.data.results);

      console.log(this.items);

      this.count = item.data.count;
    }
}

</script>
