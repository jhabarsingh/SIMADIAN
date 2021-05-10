<template>
  <v-app id="inspire">
    <List :drawer="drawer" />
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>SIMADIAN</v-toolbar-title>
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
