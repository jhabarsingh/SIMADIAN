<template>
  <v-card
    class="mx-auto"
    max-width="344"
  >
    <v-img
      src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
      height="200px"
    ></v-img>

    <v-card-title
        style="display:flex;justify-content:center;"
    >
      SIMADIAN
    </v-card-title>
        👋
    <v-card-subtitle>
      
    </v-card-subtitle>

    <v-card-actions
        style="padding-bottom: 20px;"
    >
      <v-btn
        color="orange lighten-2"
        text
        @click="$store.state.dialog = true"
      >
        Logout
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text
        >
          Gratitude is the healthiest of all human emotions. The more you express gratitude for what you have, the more likely you will have even more to express gratitude for.
        </v-card-text>
      </div>
    </v-expand-transition>

    <LogoutConfirm />
  </v-card>
</template>


<script>
  import LogoutConfirm from './LogoutConfirm.vue'
  export default {
    components: {
      LogoutConfirm,
    },
    data: () => ({
      show: false,
    }),
    methods: {
    }
  }
</script>