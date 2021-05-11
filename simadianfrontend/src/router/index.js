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
    path: '/inbox',
    name: 'Inbox',
    component: () => import('../components/items/Inbox.vue')
  },
  {
    path: '/favourite',
    name: 'Favourite',
    component: () => import('../components/items/Favourite.vue')
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
