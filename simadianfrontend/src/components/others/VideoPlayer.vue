<template>
  <div
    style="width:100vw;display:flex;justify-content:center;"
  >
      <video-player  
        class="video-player-box"
        ref="videoPlayer"
        :options="playerOptions"
        :playsinline="true"
        customEventName="customstatechangedeventname"
        style="padding:20px;"
    >
    </video-player>
  </div>
</template>
 
<script>
  // Similarly, you can also introduce the plugin resource pack you want to use within the component
  // import 'some-videojs-plugin'
  export default {
    data() {
      return {
        playerOptions: {
          // videojs options
          muted: true,
          language: 'en',
          playbackRates: [0.7, 1.0, 1.5, 2.0],
          sources: [{
            type: "video/mp4",
            src: "https://cdn.theguardian.tv/webM/2015/07/20/150716YesMen_synd_768k_vp8.webm"
          }],
          poster: "https://i.pinimg.com/originals/dd/12/95/dd1295c8b9db4fc6958dc2a72d91c8ff.jpg",
        }
      }
    },
    mounted() {
      
    },
    computed: {
      player() {
        return this.$refs.videoPlayer.player
      }
    },
    methods: {
    
    }
  }
</script>