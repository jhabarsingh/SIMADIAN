<template>
  <v-card
    class="mx-auto"
    width="256"
    tile
  >
    <v-navigation-drawer 
        v-model="$store.state.drawer"
        app
    >
      <v-system-bar></v-system-bar>
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <v-img src="https://raw.githubusercontent.com/jhabarsingh/SIMADIAN/main/doc/trademark.png"></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="title">
              SIMADIAN
            </v-list-item-title>
            <v-list-item-subtitle>Let's Sell it</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
          </v-list-item-action>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="selectedItem"
          color="primary"
        >
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            @click="goTo(item.route)"
            :disabled="item.disabled"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>


<script>
  export default {
    data: () => ({
      selectedItem: 0,
      items: [
        { text: 'Home', icon: 'mdi-home', route: 'home' , disabled: false},
        { text: 'Received', icon: 'mdi-history', route: 'received', disabled: (localStorage.getItem("access") ? false: true) },
        { text: 'Sent', icon: 'mdi-star', route: 'sent', disabled: (localStorage.getItem("access") ? false: true) },
        { text: 'Update Profile', icon: 'mdi-cloud-upload', route: 'update-profile', disabled: (localStorage.getItem("access") ? false: true) },
        { text: 'Upload Books', icon: 'mdi-upload', route: 'upload-item', disabled: (localStorage.getItem("access") ? false: true) },
        { text: 'Videos', icon: 'mdi-file', route: 'videos' , disabled: false},
      ],
    }),
    props: [
        "drawer",
    ],

    methods: {
      goTo(url) {
        this.$store.state.drawer = !this.$store.state.drawer
        this.$router.push(`/${url}`)
      }
    },
  }
</script>