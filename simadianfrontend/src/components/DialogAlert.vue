
<template>
  <div class="text-center">
    <v-dialog
      v-model="$store.state.dialog"
      width="600"
    >

      <v-card>
        <v-card-title class="headline primary"
            style="text-transform:uppercase; color:white"
        >
            {{ $store.state.dialogDetail.heading }}
        </v-card-title>


        <v-card-text
            style="text-align:justify;"
        >
            <v-list-item-group
                color="primary"
            >
                <v-list-item
                    v-for="(item, i) in $store.state.dialogDetail.details"
                    :key="i"
                >
                    <v-list-item-content>
                        <v-list-item-title v-text="item"
                            style="font-size:15px;margin:5px;text-transform:capitalize;"
                        ></v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
         </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="$store.state.dialog = false"
          >
            Close
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
  export default {
    data () {
      return {
     
      }
    },
    methods: {
           
    }
  }
</script>