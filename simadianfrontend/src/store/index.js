import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    URL: "http://ec2-18-224-181-83.us-east-2.compute.amazonaws.com/",
    drawer: null,
    user: null,
    dob: null
  },
  mutations: {
  },
  actions: {
    userRegister({commit, state}, data) {
      console.log(data);
      let options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: data
      }
      fetch(state.URL + 'users/create/', options).then(res => {
          console.log(res)
      }).then(err => {
        console.log(err);
      })
    },

    userLogin({commit, state}, data) {

    },

    userLogout({commit, state}, data) {

    }
  },
  modules: {
  }
})
