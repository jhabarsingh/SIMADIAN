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

  export default {
    components: {
      DatePicker
    },
    data: () => ({
      select: null,
      valid: true,
      username: '',
      firstname: '',
      lastname: '',
      password: '',
      email: '',
      confirm_password: '',
      nameRules: [
        v => !!v || 'Name is required',
      ],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ]
    }),

    methods: {
      validate () {
        let a = this.$refs.form.validate()
        
        if(true) {

        }
      },
      handlePassword () {
        if(this.password != this.confirm_password)  {
          return 'Password mismatch'
        }
        return true;
      }
    },
  }
</script>