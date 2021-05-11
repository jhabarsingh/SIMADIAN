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
    component: () => import('../components/Register.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../components/Login.vue')
  },
  {
    path: '/detail',
    name: 'Detail',
    component: () => import('../components/items/ItemDetail.vue')
  },
  {
    path: '/sent',
    name: 'Sent',
    component: () => import('../components/items/Sent.vue')
  },
  {
    path: '/favourite',
    name: 'Favourite',
    component: () => import('../components/items/Favourite.vue')
  },
  {
    path: '/received',
    name: 'Received',
    component: () => import('../components/items/Received.vue')
  },
  {
    path: '/message-detail',
    name: 'MessageDetail',
    component: () => import('../components/items/MessageDetail.vue')
  },
  {
    path: '/write-message',
    name: 'WriteMessage',
    component: () => import('../components/items/WriteMessageCard.vue')
  },
  {
    path: '/logout',
    name: 'Logout',
    component: () => import('../components/Logout.vue')
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
