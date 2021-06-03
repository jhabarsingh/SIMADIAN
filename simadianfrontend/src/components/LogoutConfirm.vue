<template>
  <v-row justify="center">
    <v-dialog
      v-model="$store.state.dialog"
      max-width="290"
    >
      <v-card>
        <v-card-title 
          style="font-size: 15px;"
        >
          Confirm If You Want To Logout?
        </v-card-title>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="green darken-1"
            text
            @click="$store.state.dialog = false"
          >
            Disagree
          </v-btn>

           <v-btn
            color="green darken-1"
            text
            @click="logout"
          >
            Agree
          </v-btn>

        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>


<script>
  export default {
    data () {
      return {
        dialog: false,
      }
    },

    methods: {
        logout() {
            localStorage.clear();
            this.$store.state.isLoggedin = false;
            this.$store.state.dialog = false;
            this.$store.state.username = "SIMADIAN";
            
            this.$router.push('/home')
        }
    }
  }
</script>