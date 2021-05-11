<template>
  <v-parallax
    dark
    src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
    style="height:100vh;"
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
  </v-parallax>
</template>

<script>
import LogoutCard from './LogoutCard.vue';

export default {
    components: {
        LogoutCard,
    }
}

</script>