<template>
  <v-card
    max-width="700"
    class="mx-auto"
    style="margin-top:20px;opacity:.8;"
  >
    <v-card-text
    >
      <div>Send Message To</div>
      <h3 class=" text--primary">
        {{ $store.state.selectedItem.seller.email }}
      </h3>
      <div class="text--primary">
        Please Don't Send Write Abusive Language
      </div>
    </v-card-text>
  <v-form>
    <v-container>
      <v-row>
        <v-col cols="12">
          <v-textarea
            v-model="message"
            outlined
            clearable
            label="Message"
            type="text"
          >
            <template v-slot:prepend>
            </template>
            <template v-slot:append>
              <v-fade-transition leave-absolute>
                <v-progress-circular
                  v-if="loading"
                  size="24"
                  color="info"
                  indeterminate
                ></v-progress-circular>
                <img v-else width="24" height="24" src="https://raw.githubusercontent.com/jhabarsingh/SIMADIAN/main/doc/trademark.png" alt="">
              </v-fade-transition>
            </template>
          </v-textarea>

         <div
            style="display:flex;justify-content:space-between;"
         >
            <SpeechToText 
            />

             <v-btn
              color="blue-grey"
              class="ma-2 white--text"
              @click="sendMessage"
            >
            Send
            <v-icon right dark>mdi-send</v-icon>
            </v-btn>
         </div>

        </v-col>

      </v-row>
    </v-container>
  </v-form>
</v-card>
</template>

<script>
  import axios from 'axios';
  import SpeechToText from './SpeechToText.vue';
  export default {
    data: () => ({
      message: 'Hey! ',
      loading: false,
    }),
    components: {
      SpeechToText
    },

    watch: {
      '$store.state.message' (val) {
        this.message = val;
      },
    },

    methods: {
      clickMe () {
        this.loading = true
        this.message = 'Wait for it...'
        setTimeout(() => {
          this.loading = false
          this.message = 'You\'ve clicked me!'
        }, 2000)
      },
      sendMessage () {
        let url = this.$store.state.URL + "items/message/create/";
        console.log(this.$store.state.selectedItem.seller.id)
        let data = {
          receiver: this.$store.state.selectedItem.seller.id,
          content: this.message 
        }
        
        let token = localStorage.getItem("access");

        let config = {
          headers: {
              'Authorization': 'Bearer ' + token
          }
        }

        if(this.message.length != 0) {
          axios.post(url, data, config)
          .then(res => {
            this.$router.push("/sent");
          })
          .catch(err => {
             // ERROR
          })
        }
      }
    },
    
    created() {
      if(this.$store.state.selectedItem == null) {
        this.$router.push("/home");
      }
      if(localStorage.getItem("username") == this.$store.state.selectedItem.seller.email) {
          this.$router.push("/home");
      }
    }
  }
</script>