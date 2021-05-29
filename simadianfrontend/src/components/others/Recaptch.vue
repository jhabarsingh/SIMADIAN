<template>
  <vue-recaptcha sitekey="6LfD9PsaAAAAAEuEguzHJIMZJyOS-sdmGPOPLGW8" :loadRecaptchaScript="true"></vue-recaptcha>
</template>

<script>
  import VueRecaptcha from 'vue-recaptcha';
  export default {
    components: { 
      VueRecaptcha 
    }
  };
</script>