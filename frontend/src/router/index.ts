import { createRouter, createWebHistory } from "vue-router"

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/login", name: "Login", component: () => import("../views/Login.vue") },
  { path: "/dashboard", name: "Dashboard", component: () => import("../views/Dashboard.vue") },
  { path: "/archive", name: "Archive", component: () => import("../views/Archive.vue") },
  { path: "/borrow", name: "Borrow", component: () => import("../views/Borrow.vue") },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const token = localStorage.getItem("token")
  if (!token && to.name !== "Login") {
    return { name: "Login" }
  }
})

export default router
