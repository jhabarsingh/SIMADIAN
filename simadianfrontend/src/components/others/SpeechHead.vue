<template>
    <div id="app">
    <v-app id="inspire">
        <v-container fluid>
        <v-layout row wrap justify-center class="mt-4">
            <v-flex xs12 sm10 text-xs-center>
            <v-text-field
                label="The text"
                v-model="text"
                textarea
            ></v-text-field>
            </v-flex>
            <v-flex xs12 sm8 md4 text-xs-center>
               <slot
                name="speech"
               >
                 
               </slot>
            </v-flex>
        </v-layout>
        </v-container>
    </v-app>
    </div>
</template>

<script>
export default {
    
      props: {
        
        text: {
          type: [String, null],
          required: true
        },
        sentences: {

        }
      },
      methods: {
      },
      update() {
      }
    
}
</script>