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
                  v-model="thumbnail1"
                  ref="image1"
                  prepend-icon="mdi-camera"
                ></v-file-input>

                <v-img
                  v-if="thumbnail1"
                  :src="url1"
                  style="margin:20px auto; width:400px;"
                  aspect-ratio="1"
                  class="grey lighten-2"
                >
                </v-img>

                <v-file-input
                  label="Thumbnail 2"
                  @change="Preview_image2"
                  v-model="thumbnail2"
                  ref="image2"
                  prepend-icon="mdi-camera"
                ></v-file-input>

                <v-img
                  v-if="thumbnail2"
                  :src="url2"
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
                  :disabled="true"
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

                <v-text-field
                v-model="educational_institution"
                label="Education Institution"
                required
                ></v-text-field>

                

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
  import DialogAlert from '../DialogAlert.vue'
  import cities from './cities.js';
  import states from './states.js';
  import axios from 'axios';
  
  export default {
    components: {
      DatePicker,
      DialogAlert
    },
    data: vm => ({
      select: null,
      valid: true,

      category: [],
      states: [],
      countries: [
        "India"
      ],
      cities: [],
      url1: null,
      url2: null,

      name: null,
      description: null,
      writer: null,
      thumbnail1: null,
      thumbnail2: null,
      cost_price: null,
      sell_price: null,
      mobile_no: null,
      country: "India",
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

        if(this.thumbnail1 == null) return;
        if(this.isImage(this.thumbnail1.name) == false) {
            this.$refs.image1.reset();
            this.thumbnail1 = null;
            return;
        }
        this.url1 = URL.createObjectURL(this.thumbnail1)
      },
      Preview_image2() {

        if(this.thumbnail2 == null) return;
        if(this.isImage(this.thumbnail2.name) == false) {
            this.$refs.image2.reset();
            this.thumbnail2 = null;
            console.log(this.thumbnail1)
            return;
        }
        this.url2 = URL.createObjectURL(this.thumbnail2)
      },

      validate () {
        let a = this.$refs.form.validate()
        
        if(true) {
            let token = localStorage.getItem("access");

            let config = {
            headers: {
                'Content-Type': 'multipart/form-data',
                'Authorization': 'Bearer ' + token
              }
            }
            let url = this.$store.state.URL + "items/create/"
            var formData = new FormData();
            
            let data = {
              name: this.name,
              description: this.discription,
              writer: this.writer,
              thumbnail1: this.thumbnail1,
              thumbnail2: this.thumbnail2,
              cost_price: this.cost_price,
              sell_price: this.sell_price,
              mobile_no: this.mobile_no,
              country: this.country,
              state: this.state,
              city: this.city,
              landmark: this.landmark,
              educational_institution: this.educational_institution
            }

            for(let i in data) {
              formData.append(i, data[i]);
            }

            axios.post(url, formData, config)
              .then(res => {
                console.log(res);
                window.location.reload;
              })
              .then(res => {
                console.log(res);
              })
              .catch(err => {
                console.log(err);
            })
        }
      },
      getExtension(filename) {
        var parts = filename.split('.');
        return parts[parts.length - 1];
      },

      isImage(filename) {
        var ext = this.getExtension(filename);
        switch (ext.toLowerCase()) {
          case 'jpg':
          case 'jpeg':
          case 'png':
          case 'svg':
          case 'gif':
            // etc
            return true;
          }
          return false;
        }
    },

    created () {
      this.states  = states.sort();
      this.cities = cities.sort();
    }
  }
</script>