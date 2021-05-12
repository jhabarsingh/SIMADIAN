<template>
  <v-card
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        class="text-center"
        cols="12"
      >
        <LogoutCard />
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import LogoutCard from './LogoutCard.vue';

export default {
    components: {
        LogoutCard,
    }
}

</script>