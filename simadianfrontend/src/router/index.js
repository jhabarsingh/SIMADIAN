import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import HomeLogin from '../views/HomeLogin.vue'
import store from '../store/index.js';

import axios from 'axios';


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/home',
    name: 'HomeLogin',
    component: HomeLogin
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            router.push('/home')
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        next();
      }
      else {
        next();
      }
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            router.push('/home')
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        next();
      }
      else {
        next();
      }
    }
  },
  {
    path: '/detail',
    name: 'Detail',
    component: () => import('../views/ItemDetail.vue')
  },
  {
    path: '/sent',
    name: 'Sent',
    component: () => import('../views/Sent.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            next();
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        router.push("/login");
      }
      else {
        router.push("/login");
      }
    }
  },
  // {
  //   path: '/favourite',
  //   name: 'Favourite',
  //   component: () => import('../views/Favourite.vue')
  // },
  {
    path: '/received',
    name: 'Received',
    component: () => import('../views/Inbox.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            next();
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        router.push("/login");
      }
      else {
        router.push("/login");
      }
    }
  },
  {
    path: '/message-detail',
    name: 'MessageDetail',
    component: () => import('../views/MessageDetail.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            next();
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        router.push("/login");
      }
      else {
        router.push("/login");
      }
    }
  },
  {
    path: '/write-message',
    name: 'WriteMessage',
    component: () => import('../views/WriteMessage.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            next();
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        router.push("/login");
      }
      else {
        router.push("/login");
      }
    }
  },
  {
    path: '/update-profile',
    name: 'UserUpdate',
    component: () => import('../views/UserUpdate.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            next();
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        router.push("/login");
      }
      else {
        router.push("/login");
      }
    }
  },
  {
    path: '/logout',
    name: 'Logout',
    component: () => import('../views/Logout.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            next();
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        router.push("/login");
      }
      else {
        router.push("/login");
      }
    }
  },
  {
    path: '/upload-item',
    name: 'UploadItems',
    component: () => import('../views/UploadItems.vue'),
    async beforeEnter(to, from, next) {
      
      if(localStorage.getItem("access")) {
        //check token validation
        let url = store.state.URL + "api/token/verify/"
        
        try {
          let data = await axios.post(url, {
            "token": localStorage.getItem("access")
          });

          data = data.data;
          
          if(Object.keys(data).length === 0) {
            next();
            return;
          }
        }
        catch(err) {
          // ERROR
        }
        localStorage.clear();
        router.push("/login");
      }
      else {
        router.push("/login");
      }
    }
  },
  {
    path: '/videos',
    name: 'Videos',
    component: () => import('../views/MyFiles.vue')
  },
  {
    path: '/test',
    name: 'Test',
    component: () => import('../components/others/Test.vue')
  },
  {
    path: '/media-player',
    name: 'MediaPlayer',
    component: () => import('../views/MediaPlayer.vue')
  },
  {
    path: '*',
    name: 'NotFound',
    component: () => import('../views/NotFound.vue')
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
