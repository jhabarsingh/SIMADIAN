import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import HomeLogin from '../views/HomeLogin.vue'
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
    component: () => import('../views/Register.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/detail',
    name: 'Detail',
    component: () => import('../views/ItemDetail.vue')
  },
  {
    path: '/sent',
    name: 'Sent',
    component: () => import('../views/Sent.vue')
  },
  {
    path: '/favourite',
    name: 'Favourite',
    component: () => import('../views/Favourite.vue')
  },
  {
    path: '/received',
    name: 'Received',
    component: () => import('../views/Inbox.vue')
  },
  {
    path: '/message-detail',
    name: 'MessageDetail',
    component: () => import('../views/MessageDetail.vue')
  },
  {
    path: '/write-message',
    name: 'WriteMessage',
    component: () => import('../views/WriteMessage.vue')
  },
  {
    path: '/update-profile',
    name: 'UserUpdate',
    component: () => import('../views/UserUpdate.vue')
  },
  // {
  //   path: '/search-filter',
  //   name: 'SearchFilter',
  //   component: () => import('../views/SearchFilter.vue')
  // },
  {
    path: '/logout',
    name: 'Logout',
    component: () => import('../views/Logout.vue')
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
