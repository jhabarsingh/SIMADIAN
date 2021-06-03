<template>
  <div>
    <v-card
      class="mx-auto"
      max-width="1000"
      style="margin-top: 20px"
    >
      <v-toolbar
        color="pink"
        dark
      >

        <v-toolbar-title>Received</v-toolbar-title>

        <v-spacer></v-spacer>

      </v-toolbar>

      <v-list two-line>
        <v-list-item-group
          v-model="selected"
          active-class="pink--text"
          multiple
        >
          <template v-for="(item, index) in items">
            <v-list-item :key="item.title" @click="goTo(item)">
              <template v-slot:default="{  }">
                <v-list-item-content>
                  <v-list-item-title v-text="item.sender.username"></v-list-item-title>


                  <v-list-item-subtitle v-text="item.content"></v-list-item-subtitle>
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
  import axios from 'axios';

  export default {
    data: () => ({
      selected: [2],
      items: [],
      page: null,
      count: null
    }),

    methods: {
      goTo(message) {
        this.$router.push({
          name: 'MessageDetail',
          query: {
            receiver: message.sender.username,
            content: message.content
          }
        })
      }
    },

    watch: {
      'page' (val) {
        this.$router.push({
          name: 'Received', 
          query: {
            page: val
          }
        }).catch(err => {

        })
      }
    },

    async created() {
      let item;
      let token = localStorage.getItem("access");

      let config = {
      headers: {
          'Content-Type': 'multipart/form-data',
          'Authorization': 'Bearer ' + token
        }
      }

      if(this.$route.query.page) {
        item = await axios.get(this.$store.state.URL + "items/message/received/" + '?page=' + this.$route.query.page, config)
        this.page = +this.$route.query.page;
      }
      else {
        item = await axios.get(this.$store.state.URL + "items/message/received/", config)      
      }
      this.items = (item.data.results);

      this.count = item.data.count;
      console.log(this.items);

    }
  }
</script>