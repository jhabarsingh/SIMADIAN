<template>
  <v-card class="text-center"
    style="margin: 0px auto 10px auto;padding:10px;display:flex;justify-content:center;"
    max-width="700px"
  >
    <v-file-input
        multiple
        label="Upload Files"
    ></v-file-input>
    <v-btn
        class="mx-2"
        fab
        dark
        small
        color="primary"
    >
    <v-icon dark>
      mdi-upload
      </v-icon>
    </v-btn>
  </v-card>
</template>