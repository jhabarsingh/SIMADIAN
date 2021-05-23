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
                v-model="name"
                :counter="10"
                :rules="nameRules"
                label="Username"
                required
                ></v-text-field>

                <v-text-field
                v-model="name"
                :counter="10"
                :rules="nameRules"
                label="First Name"
                required
                ></v-text-field>

                <v-text-field
                v-model="name"
                :counter="10"
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
                v-model="email"
                :rules="emailRules"
                label="Password"
                required
                type="password"
                ></v-text-field>

                <v-text-field
                v-model="email"
                :rules="emailRules"
                label="Confirm Password"
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
      valid: true,
      name: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => (v && v.length <= 10) || 'Name must be less than 10 characters',
      ],
      email: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      select: null,
      items: [
        'Item 1',
        'Item 2',
        'Item 3',
        'Item 4',
      ],
      checkbox: false,
    }),

    methods: {
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
  }
</script>