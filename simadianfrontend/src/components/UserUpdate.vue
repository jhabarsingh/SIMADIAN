<template>
    <v-card
        style="max-width:800px;margin:auto;"
    >
        <template>
          <center 
            style="padding:10px;font-size:30px;text-transform:uppercase;"
          >
            Update Details
          </center>

           <v-divider />
          
            <v-form
                ref="form"
                v-model="valid"
                lazy-validation
                style="padding:30px;"
            >
                <v-text-field
                v-model="username"
                :rules="nameRules"
                label="Username"
                required
                :disabled="true"
                ></v-text-field>

                <v-text-field
                v-model="firstname"
                :rules="nameRules"
                label="First Name"
                required
                ></v-text-field>

                <v-text-field
                v-model="lastname"
                :rules="nameRules"
                label="Last Name"
                required
                ></v-text-field>


                <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                required
                :disabled="true"
                ></v-text-field>
                

                <DatePicker />

                <v-text-field
                v-model="password"
                label="Password"
                required
                type="password"
                ></v-text-field>

                <v-text-field
                v-model="confirm_password"
                label="Confirm Password"
                :rules="[handlePassword]"
                required
                type="password"
                ></v-text-field>

                <v-btn
                :disabled="!valid"
                color="primary"
                class="mr-4"
                @click="validate"
                >
                Update
                </v-btn>

            </v-form>
            </template>

            <DialogAlert />
    </v-card>
</template>

<script>
  import axios from 'axios';
  import DatePicker from './DatePicker.vue'
  import EventBus from './event-bus';
  import DialogAlert from './DialogAlert.vue'
  export default {
    components: {
      DatePicker,
      DialogAlert
    },
    data: vm => ({
      select: null,
      valid: true,
      username: '',
      firstname: '',
      lastname: '',
      password: '',
      email: '',
      confirm_password: '',
      date_of_birth: vm.formatDate(new Date().toISOString().substr(0, 10)),
      nameRules: [
        v => !!v || 'Name is required',
      ],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ]
    }),

    methods: {
      formatDate (date) {
        if (!date) return null

        const [year, month, day] = date.split('-')
        return `${year}-${month}-${day}`
      },
      validate () {
        let a = this.$refs.form.validate()
        
        let url = this.$store.state.URL + "users/user/";
        let token = localStorage.getItem("access");
        
        if(true) {
        let config = {
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
          }
        }
        axios.put(url, {
            username: this.username,
            first_name: this.firstname,
            last_name: this.lastname,
            date_of_birth: this.date_of_birth,
            email: this.email,
            password: this.password
          }, config)
          .then(res => {
            console.log(res);
            window.location.reload;
          })
          .catch(err => {
            console.log(err);
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
    },
    async created() {
      let url = this.$store.state.URL + "users/user/";
      let token = localStorage.getItem("access");
   
      let config = {
        headers: {
          'Authorization': 'Bearer ' + token
        }
      }
            
      let res = await axios.get(url, config)

      res = res.data;
      this.username = res.username;
      this.firstname = res.first_name;
      this.lastname = res.last_name;
      this.email = res.email;
      this.date_of_birth = res.date_of_birth;
      
    }
  }
</script>