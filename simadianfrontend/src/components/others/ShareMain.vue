<template>
  <v-row justify="space-around">
    <v-col cols="auto">
      <v-dialog
        transition="dialog-top-transition"
        max-width="700px"
        min-width="700px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="grey lighten-3"
            v-bind="attrs"
            v-on="on"
            fab
            elevation="4"
          >
            <v-icon
              large
            >
              mdi-share
            </v-icon>
          </v-btn>
        </template>
        <template v-slot:default="dialog">
          <v-card
            max-width="700px"
            min-width="700px"
          >
              <Share />
          </v-card>
        </template>
      </v-dialog>
    </v-col>
  </v-row>
</template>


<script>
import Share from './Share';

export default {
  components: {
    Share,
  }
}
</script>