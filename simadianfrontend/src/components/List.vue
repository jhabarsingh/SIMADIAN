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
            @click="$router.push(`/${item.route}`)"
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
        { text: 'Home', icon: 'mdi-home', route: 'home' },
        { text: 'Favourite ', icon: 'mdi-account-multiple', route: 'favourite' },
        { text: 'Inbox', icon: 'mdi-history', route: 'received' },
        { text: 'Sent', icon: 'mdi-star', route: 'sent' },
        { text: 'Search Filter', icon: 'mdi-cloud-upload', route: 'search-filter' },
        { text: 'Logout', icon: 'mdi-logout', route: 'logout' },
      ],
    }),
    props: [
        "drawer",
    ]
  }
</script>