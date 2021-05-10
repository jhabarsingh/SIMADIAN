<template>
  <v-app id="inspire">
    <List :drawer="drawer" />
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

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

    <v-main>

    </v-main>
  </v-app>
</template>

<script>
  import List from './List';
  export default {
    components: {
      List,
    },
    data: () => ({ drawer: null }),
  }
</script>
