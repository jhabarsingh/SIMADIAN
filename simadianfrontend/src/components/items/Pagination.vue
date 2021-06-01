<template>
  <div class="text-center">
    <v-container>
      <v-row justify="center">
        <v-col cols="8">
          <v-container class="max-width">
            <v-pagination
              v-model="page"
              class="my-4"
              :length="count / 10"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>


<script>
  export default {
    props: [
      'count',
    ],
    data () {
      return {
        page: 1,
      }
    },
  }
</script>