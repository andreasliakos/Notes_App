import { createRouter, createWebHistory } from 'vue-router'
import Note from '../components/Note.vue'
import Home from '../views/App.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/note/:id',
    name: 'Note',
    component: Note,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
