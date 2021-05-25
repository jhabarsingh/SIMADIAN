<template>
    <v-card
        style="max-width:800px;margin:auto;"
    >
        <template>
          <center 
            style="padding:10px;font-size:30px;text-transform:uppercase;"
          >
            Sign Up
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
                Validate
                </v-btn>

            </v-form>
            </template>
    </v-card>
</template>

<script>
  import DatePicker from './DatePicker.vue'
  import EventBus from './event-bus';

  export default {
    components: {
      DatePicker
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
        return `${month}/${day}/${year}`
      },
      validate () {
        let a = this.$refs.form.validate()
        
        if(true) {
         this.$store.dispatch('userRegister', JSON.stringify({
            username: this.username,
            first_name: this.firstname,
            last_name: this.lastname,
            date_of_birth: this.date_of_birth,
            email: this.email,
            password: this.password
          }));
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