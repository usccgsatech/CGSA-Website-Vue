import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CGSAIntro from '../views/CGSAIntro.vue'
import Contact from '../views/Contact.vue'
import BoardMembers from '../views/BoardMembers.vue'
import Departments from '../views/Departments.vue'
import Welfare from '../views/Welfare.vue'
import Career from '../views/Career.vue'
import Activity from '../views/Activity.vue'
import Alumni from '../views/Alumni.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about/cgsa-intro',
      name: 'cgsa-intro',
      component: CGSAIntro
    },
    {
      path: '/about/board-members',
      name: 'board-members',
      component: BoardMembers
    },
    {
      path: '/about/departments',
      name: 'departments',
      component: Departments
    },
    {
      path: '/welfare',
      name: 'welfare',
      component: Welfare
    },
    {
      path: '/career',
      name: 'career',
      component: Career
    },
    {
      path: '/activity',
      name: 'activity',
      component: Activity
    },
    {
      path: '/alumni',
      name: 'alumni',
      component: Alumni
    },
    {
      path: '/contact',
      name: 'contact',
      component: Contact
    }
  ],
})

export default router
