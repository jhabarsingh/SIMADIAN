<template>
    <v-card
      style="display:flex;justify-content:space-evenly;margin:auto;padding-top:7px;"
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
            :src="`https://github.com/jhabarsingh/SIMADIAN/blob/main/simadianfrontend/src/assets/logos/${platform}.png?raw=true`" 
            width="100px"
        />
    </ShareNetwork>
    </v-card>
</template>

<script>
export default {
  props: [
    'url',
  ],
  data () {
    return {
      title: "Watch More Video On Simdian",
      description: "Video From Simadian",
      quote: "Books are wisdom",
      hashtags: "#Simadian",

      social_platforms: [
        'whatsapp',
        'facebook',
        'reddit',
        'linkedin',
        'twitter'
      ]
    }
  }
}
</script>