import { createRouter, createWebHistory } from 'vue-router'

const routes = [{
        path: '/login',
        name: 'login',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/AccountLogin.vue')
    },
    {
        path: '/', // Redirection, si l'URL est vide alors redirection vers la page login
        redirect: { name: 'login' }
    },
    {
        path: '/redirect',
        name: 'redirect',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/RedirectToViews.vue')
    },
    {
        path: '/teacher',
        name: 'teacher',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/TeacherViews.vue')
    },
    {
        path: '/student',
        name: 'student',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/StudentViews.vue')
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router