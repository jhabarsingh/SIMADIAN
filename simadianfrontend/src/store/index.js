import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router/index.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    URL: "http://localhost:8000/",
    drawer: null,
    user: null,
    dialog: false, 
    dialogDetail: {
      "heading": "Instructions",
      "details": [
        "Hi"
      ]
    }
  },
  mutations: {
    changeDialog(state, {heading, details}) {
      state.dialogDetail.heading = heading;
      state.dialogDetail.details = details; 
    }
  },
  actions: {
    async userRegister({commit, state}, data) {
      try {
        let res = await axios.post(state.URL + 'users/create/', data)
        return res;
      } catch (err) {
        throw err;
      }
    },

    userLogin({commit, state}, data) {

    },

    userLogout({commit, state}, data) {

    }
  },
  modules: {
  }
})
