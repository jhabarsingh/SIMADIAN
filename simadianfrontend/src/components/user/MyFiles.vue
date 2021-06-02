<template>
  <div>
      <MultipleFileUpload />
  <v-card
    class="mx-auto"
    max-width="1000"
    style="margin-top: 20px"
  >
    <v-toolbar
      color="pink"
      dark
    >

      <v-toolbar-title>Files</v-toolbar-title>

      <v-spacer></v-spacer>

    </v-toolbar>

    <v-list two-line>
      <v-list-item-group
        v-model="selected"
        active-class="pink--text"
        multiple
      >
        <template v-for="(item, index) in items">
          <v-list-item :key="item.title" @click="goTo(item.file)">
            <template >
              <v-list-item-content>

                <v-list-item-subtitle v-text="item.file"></v-list-item-subtitle>

              </v-list-item-content>
            </template>
          </v-list-item>

          <v-divider
            v-if="index < items.length - 1"
            :key="index"
          ></v-divider>
        </template>
      </v-list-item-group>
    </v-list>
  </v-card>
  <pagination :count=count />
  </div>
</template>

<script>
import axios from 'axios';

import MultipleFileUpload from './MultipleFileUpload.vue';
import Pagination from '../items/Pagination.vue';

  export default {
    components: {
        MultipleFileUpload,
        Pagination
    },
    data: () => ({
      selected: [2],
      items: [],
      count: 0,
    }),

    methods: {
        goTo(url) {
          this.$router.push({
            name: 'MediaPlayer',
            query: {
              link: url
            }
          });
        },
    },
    async created() {
      let item = await axios.get(this.$store.state.URL + "items/files/")      

      this.items = (item.data.results);

      this.items = this.items.filter(el => el.file != null);
      this.count = item.data.count;

    }
  }
</script>