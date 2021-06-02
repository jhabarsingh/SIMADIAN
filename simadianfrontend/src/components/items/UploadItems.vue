<template>
    <v-card
        style="max-width:800px;margin:auto;"
    >
        <template>
          <center 
            style="padding:10px;font-size:30px;text-transform:uppercase;"
          >
            Upload Book
          </center>

           <v-divider />
          
            <v-form
                ref="form"
                v-model="valid"
                lazy-validation
                style="padding:30px;"
            >

                <v-text-field
                v-model="name"
                label="Book Name"
                required
                ></v-text-field>

                <v-textarea
                  solo
                  name="input-7-4"
                  label="Description"
                  v-model="description"
                ></v-textarea>

                <v-text-field
                v-model="writer"
                label="Writer Name"
                required
                ></v-text-field>


                <v-file-input
                  label="Thumbnail 1"
                  @change="Preview_image1"
                  filled
                  v-model="thumbnail1"
                  prepend-icon="mdi-camera"
                ></v-file-input>

                <v-img
                  v-if="thumbnail1"
                  :src="url1"
                  style="margin:20px auto; width:400px;"
                  :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
                  aspect-ratio="1"
                  class="grey lighten-2"
                >
                </v-img>

                <v-file-input
                  label="Thumbnail 2"
                  @change="Preview_image2"
                  filled
                  v-model="thumbnail2"
                  prepend-icon="mdi-camera"
                ></v-file-input>

                <v-img
                  v-if="thumbnail2"
                  :src="url2"
                  :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
                  style="margin:20px auto; width:400px;"
                  aspect-ratio="1"
                  class="grey lighten-2"
                >
                </v-img>
                
                <v-text-field
                v-model="cost_price"
                label="Cost Price"
                required
                ></v-text-field>


                <v-text-field
                v-model="sell_price"
                label="Sell Price"
                required
                ></v-text-field>

                <v-text-field
                v-model="mobile_no"
                label="Mobile No"
                ></v-text-field>

                <v-select
                  :items="countries"
                  label="Country"
                  v-model="country"
                  solo
                ></v-select>

                <v-select
                  :items="states"
                  label="State"
                  v-model="state"
                  solo
                ></v-select>

                <v-select
                  :items="cities"
                  label="City"
                  v-model="city"
                  solo
                ></v-select>

                <v-text-field
                v-model="landmark"
                label="Land Mark"
                required
                ></v-text-field>

                <v-select
                  :items="educational_institutions"
                  label="Education Institute"
                  v-model="educational_institutions"
                  solo
                ></v-select>
                

                <v-btn
                :disabled="!valid"
                color="primary"
                class="mr-4"
                @click="validate"
                >
                  Upload
                </v-btn>

            </v-form>
            </template>

            <DialogAlert />
    </v-card>
</template>

<script>
  import DatePicker from '../DatePicker.vue'
  import EventBus from '../event-bus';
  import DialogAlert from '../DialogAlert.vue'
  export default {
    components: {
      DatePicker,
      DialogAlert
    },
    data: vm => ({
      select: null,
      valid: true,

      category: [],
      name: null,
      url1: null,
      url2: null,
      description: null,
      writer: null,
      thumbnail1: null,
      thumbnail2: null,
      cost_price: null,
      sell_price: null,
      mobile_no: null,
      country: null,
      state: null,
      city: null,
      landmark: null,
      educational_institution: null,
      
      nameRules: [
        v => !!v || 'Name is required',
      ]
    }),

    methods: {
      Preview_image1() {
        this.url1 = URL.createObjectURL(this.thumbnail1)
      },
      Preview_image2() {
        this.url2 = URL.createObjectURL(this.thumbnail2)
      },
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${year}-${month}-${day}`
      },
      validate () {
        let a = this.$refs.form.validate()
        
        if(true) {
         this.$store.dispatch('userRegister', {
            username: this.username,
            first_name: this.firstname,
            last_name: this.lastname,
            date_of_birth: this.date_of_birth,
            email: this.email,
            password: this.password
          })
          
          .then(res => {
            this.$router.push("/login");
          })
          
          .catch(err => {
            this.$store.commit('changeDialog', {
              'heading': 'Instructions',
              details: [
                'username should not be blank',
                'username and email should be unique',
                'email should be valid',
                'password should contain alphabet, number and punctuation',
                'password shouldn\'t match with your name'
              ]
            })
            this.$store.state.dialog = true;
          })
        }
      },
      handlePassword () {
        if(this.password != this.confirm_password)  {
          return 'Password mismatch'
        }
        return true;
      }
    },

    mounted () {
      EventBus.$on('EVENT_NAME', function (payLoad) {
        this.date_of_birth = payLoad;
      });
    }
  }
</script>