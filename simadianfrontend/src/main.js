import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import VueSocialSharing from 'vue-social-sharing'
import VueVideoPlayer from 'vue-video-player'
 
// require videojs style
import 'video.js/dist/video-js.css'

Vue.use(VueSocialSharing);

Vue.config.productionTip = false
Vue.use(VueVideoPlayer)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
