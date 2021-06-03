<template>
  <v-hover>
    <template v-slot:default="{ hover }">
      <v-card
        class="mx-auto"
      >
        <div
          style="height:250px;overflow:hidden;"
        >
          <v-img 
            style="height:300px;"
            :src="thumbnail[0]"
          ></v-img>
        </div>

        <v-card-text>
          <h2 class="title primary--text"
            style="text-transform: Capitalize"
          >
            {{ title }}
          </h2>
            {{ description }}
        </v-card-text>

        <v-card-title>
            <v-chip-group
              v-for="(val, i) in category"
              :key="i"
            >
              <v-chip>{{ val }}</v-chip>

            </v-chip-group>
        </v-card-title>

         <v-divider />


        <v-list-item>

          <v-list-item-content>
            <v-list-item-title>Writer Name</v-list-item-title>
            <v-list-item-subtitle>
                    <v-chip
                      color="primary"
                      small
                    >
                      {{ writer }}
                    </v-chip>

            </v-list-item-subtitle>
          </v-list-item-content>
         
          <v-list-item-content>
            <v-list-item-title>Cost Price</v-list-item-title>
            <v-list-item-subtitle>
                    <v-chip
                      color="primary"
                      small
                    >
                      {{ cost_price }} INR
                    </v-chip>
            </v-list-item-subtitle>
          </v-list-item-content>
         
          <v-list-item-content>
            <v-list-item-title>Sell Price</v-list-item-title>
            <v-list-item-subtitle>
                      <v-chip
                        color="primary"
                        small
                      >
                        {{ sell_price }} INR
                      </v-chip>
            </v-list-item-subtitle>
          </v-list-item-content>
        
        </v-list-item>

        
        <v-fade-transition>
          <v-overlay
            v-if="hover"
            absolute
            style="z-index:0;"
            color="#036358"
          >
            <v-btn @click="$router.push('/detail')">See more info</v-btn>
          </v-overlay>
        </v-fade-transition>
      </v-card>
    </template>
  </v-hover>
</template>

<script>
  import Carousal from './Carousal.vue'
  export default {
    components: {
      Carousal
    },
    props: [
      'title',
      'description',
      'thumbnail',
      'cost_price',
      'sell_price',
      'writer',
      'category'
    ],
    data: () => ({
      overlay: false,
    }),
  }
</script>