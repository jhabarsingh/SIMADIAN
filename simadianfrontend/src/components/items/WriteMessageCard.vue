<template>
  <v-parallax
    dark
    src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
    style="min-height:100vh;"
  >
    <v-row
      align="center"
      justify="center"
    >
      <v-col class="text-center" cols="12">
        <write-message />
      </v-col>
    </v-row>
  </v-parallax>
</template>

<script>
import WriteMessage from './WriteMessage.vue';

export default {
  data: () => ({

  }),
  components: {
    WriteMessage,
  },
}

</script>
