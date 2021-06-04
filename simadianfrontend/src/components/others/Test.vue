<template>
    <v-card
      style="display:flex;justify-content:space-evenly;max-width:700px;margin:auto;"
    >
    <ShareNetwork
        v-for="(platform, index) in social_platforms"
        :key="index"
        :network="platform"
        :url="url"
        :title="title"
        :description="description"
        :quote="quote"
        :hashtags="hashtags"
    >
        <img 
            :src="require(`../../assets/logos/${platorm}.png`)" 
            width="100px"
        />
    </ShareNetwork>
    </v-card>
</template>

<script>
export default {
  data () {
    return {
      url: "https://news.vuejs.org/issues/180",
      title: "Say hi to Vite! A brand new, extremely fast development setup for Vue.",
      description: "This week, I’d like to introduce you to 'Vite', which means 'Fast'. It’s a brand new development setup created by Evan You.",
      quote: "The hot reload is so fast it\'s near instant. - Evan You",
      hashtags: "vuejs,vite",

      social_platforms: [
        'whatsapp',
        'facebook',
        'redit',
        'linkedin',
        'twitter'
      ]
    }
  }
}
</script>