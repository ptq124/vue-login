import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: () => import('./views/LoginForm.vue') },
    { path: '/todo', component: () => import('./views/TodoList.vue') },
  ],
})

export default router
