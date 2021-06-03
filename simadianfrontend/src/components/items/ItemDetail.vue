<template>
  <v-hover v-slot="{ hover }"
    style="margin-top:20px;"
  >
    <v-card
      class="mx-auto"
      color="grey lighten-4"
      max-width="600"
    >
      <v-img
        :aspect-ratio="16/9"
        :src="$store.state.selectedItem.thumbnail2"
      >
        <v-expand-transition>
          <div
            v-if="hover"
            class="d-flex transition-fast-in-fast-out orange darken-2 v-card--reveal display-3 white--text"
            style="height: 100%;"
          >
            {{ $store.state.selectedItem.sell_price }} INR
          </div>
        </v-expand-transition>
      </v-img>
      <v-card-text
        class="pt-6"
        style="position: relative;"
      >
        <v-btn
          absolute
          color="orange"
          class="white--text"
          fab
          large
          right
          top
          @click="$router.push('/write-message')"
        >
          <v-icon>mdi-message</v-icon>
        </v-btn>
        <div class="font-weight-light grey--text title mb-2">
          Writter  : 
            <v-chip
              color="primary"
              small
            >
              {{ $store.state.selectedItem.writer }}
            </v-chip>
        </div>
        <h3 class="display-1 font-weight-light orange--text mb-2">
          {{ $store.state.selectedItem.name }}
        </h3>
        <div class="font-weight-light title mb-2">
          {{ $store.state.selectedItem.description }}
        </div>
      </v-card-text>
    </v-card>
  </v-hover>
</template>

<script>
import Carousal from './Carousal.vue';

export default {
  components: {
    Carousal
  },
  data () {
    return {
      slides: []
    }
  },
  created() {
      if(this.$store.state.selectedItem == null) {
        this.$router.push("/home");
      }
      else {
        this.slides.push(this.$store.state.selectedItem.thumbnail1);
        this.slides.push(this.$store.state.selectedItem.thumbnail2)
      }
    }
}
</script>

<style>
    .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .5;
    position: absolute;
    width: 100%;
    }
</style>