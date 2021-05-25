import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    URL: "http://localhost:8000/",
    drawer: null,
    user: null
  },
  mutations: {
  },
  actions: {
    userRegister({commit, state}, data) {
      console.log(data);
      
      axios.post(state.URL + 'users/create', data)
      .then(data => {
        console.log(data);
      }).then(err =>{
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
