import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Greenland = () => import('@/views/greenland/index.vue')
const Streettree = () => import('@/views/streettree/index.vue')
const Flowerbed = () => import('@/views/flowerbed/index.vue')
const Nursery = () => import('@/views/nursery/index.vue')
const Irrigation = () => import('@/views/irrigation/index.vue')
const Pruning = () => import('@/views/pruning/index.vue')
const Pest = () => import('@/views/pest/index.vue')
const Fertilize = () => import('@/views/fertilize/index.vue')
const Replant = () => import('@/views/replant/index.vue')
const Ancient = () => import('@/views/ancient/index.vue')
const Patrol = () => import('@/views/patrol/index.vue')
const Rectify = () => import('@/views/rectify/index.vue')
const Facility = () => import('@/views/facility/index.vue')
const Accept = () => import('@/views/accept/index.vue')
const Plan = () => import('@/views/plan/index.vue')
const Season = () => import('@/views/season/index.vue')
const Waterbody = () => import('@/views/waterbody/index.vue')
const Record = () => import('@/views/record/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/greenland', name: 'greenland', component: Greenland },
    { path: '/streettree', name: 'streettree', component: Streettree },
    { path: '/flowerbed', name: 'flowerbed', component: Flowerbed },
    { path: '/nursery', name: 'nursery', component: Nursery },
    { path: '/irrigation', name: 'irrigation', component: Irrigation },
    { path: '/pruning', name: 'pruning', component: Pruning },
    { path: '/pest', name: 'pest', component: Pest },
    { path: '/fertilize', name: 'fertilize', component: Fertilize },
    { path: '/replant', name: 'replant', component: Replant },
    { path: '/ancient', name: 'ancient', component: Ancient },
    { path: '/patrol', name: 'patrol', component: Patrol },
    { path: '/rectify', name: 'rectify', component: Rectify },
    { path: '/facility', name: 'facility', component: Facility },
    { path: '/accept', name: 'accept', component: Accept },
    { path: '/plan', name: 'plan', component: Plan },
    { path: '/season', name: 'season', component: Season },
    { path: '/waterbody', name: 'waterbody', component: Waterbody },
    { path: '/record', name: 'record', component: Record },
  ],
})

export default router
