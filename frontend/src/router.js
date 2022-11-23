import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const requireAuth = () => (to,from,next)=>{
  const token = localStorage.getItem('access_token')

  if(token){
    return next()
  }
  next('/')
}

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: () => import('./views/LoginForm.vue') },
    { path: '/todo', component: () => import('./views/TodoList.vue'), beforeEnter:requireAuth() },
  ],
})

export default router

