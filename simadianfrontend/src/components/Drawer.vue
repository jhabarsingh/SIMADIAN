<template>
  <v-app id="inspire"
  >
    <List />
    <v-app-bar app>
      <v-app-bar-nav-icon @click="$store.state.drawer = !$store.state.drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>
        <v-tab>
          <v-badge
            color="pink"
            dot
          >
            SIMADIAN
          </v-badge>
        </v-tab>
      </v-toolbar-title>

      <v-divider style="margin: 0px 10px;" />

      <v-btn
        class="ma-2"
        color="primary"
        dark
        rounded
        @click="$router.push('/login')"
      >
        Login
        <v-icon
          dark
          right
        >
          mdi-login
        </v-icon>
      </v-btn>

      <v-btn
        class="ma-2"
        color="warning"
        dark
        rounded
        @click="$router.push('/register')"
      >
        Sign Up
        <v-icon
          dark
          right
        >
          mdi-account
        </v-icon>
      </v-btn>

    </v-app-bar>

    <v-main
    >
        <slot
            name="main"
        ></slot>
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
  import List from './List';
  import Item from '../components/items/Items'
  import Footer from './Footer.vue';

  export default {
    components: {
      List,
      Item,
      Footer
    },
    data: () => ({
      
    }),
    created() {
      console.log(window.location.pathname)
    }
  }
</script>
