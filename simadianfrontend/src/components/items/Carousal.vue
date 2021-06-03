<template>
  <v-card
    elevation="24"
    max-width="444"
    class="mx-auto"
  >
    <v-system-bar lights-out></v-system-bar>
    <v-carousel
      :continuous="false"
      cycle
      :show-arrows="false"
      hide-delimiter-background
      delimiter-icon="mdi-minus"
      height="300"
    >
      <v-carousel-item
        v-for="(slide, i) in slides"
        :key="i"
      >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <v-img :src="slide"
            ></v-img>
          </v-row>
      </v-carousel-item>
    </v-carousel>
  </v-card>
</template>


<script>
  export default {
    props: [
        'slides'
    ],
    data () {
      return {
      }
    },
  }
</script>