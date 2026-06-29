<template>
  <div class="dashboard">
    <header class="topbar">
      <h1>OpenFDAMS</h1>
      <div class="user-info">
        <span>{{ username }}</span>
        <button @click="logout">退出</button>
      </div>
    </header>

    <div class="cards">
      <div class="card">
        <div class="card-icon">👤</div>
        <div class="card-label">当前用户</div>
        <div class="card-value">{{ userInfo.username || "—" }}</div>
        <div class="card-sub">角色: {{ userInfo.role || "—" }}</div>
      </div>
      <div class="card">
        <div class="card-icon">📁</div>
        <div class="card-label">档案数量</div>
        <div class="card-value">{{ stats.archives }}</div>
        <div class="card-sub">已入库档案</div>
      </div>
      <div class="card">
        <div class="card-icon">📋</div>
        <div class="card-label">借阅数量</div>
        <div class="card-value">{{ stats.borrows }}</div>
        <div class="card-sub">当前借出</div>
      </div>
      <div class="card">
        <div class="card-icon">⚙️</div>
        <div class="card-label">系统状态</div>
        <div class="card-value status-ok">正常</div>
        <div class="card-sub">生命周期: {{ lifecycle }}</div>
      </div>
    </div>

    <div class="actions">
      <button class="btn-primary" @click="$router.push('/archive')">📁 档案管理</button>
      <button class="btn-secondary" @click="$router.push('/borrow')">📋 借阅管理</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import { getMe } from "../api/auth"
import { getDashboard } from "../api/archive"

const router = useRouter()
const username = ref(localStorage.getItem("username") || "")
const userInfo = ref({ username: "", role: "" })
const stats = ref({ archives: 0, borrows: 0 })
const lifecycle = ref("active")

onMounted(async () => {
  try {
    const me = await getMe()
    userInfo.value = me
  } catch {}

  try {
    const dash = await getDashboard()
    if (dash.stats) stats.value = dash.stats
    if (dash.lifecycle?.status) lifecycle.value = dash.lifecycle.status
  } catch {}
})

function logout() {
  localStorage.removeItem("token")
  localStorage.removeItem("username")
  router.push("/login")
}
</script>

<style scoped>
.dashboard { min-height: 100vh; background: #f5f5f5; }
.topbar {
  background: #1a1a2e; color: #fff; padding: 1rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
}
.topbar h1 { font-size: 1.4rem; }
.user-info { display: flex; align-items: center; gap: 1rem; }
.user-info button {
  background: transparent; border: 1px solid #fff; color: #fff;
  padding: 0.4rem 1rem; border-radius: 6px; cursor: pointer;
}
.cards {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem; padding: 2rem;
}
.card {
  background: #fff; border-radius: 12px; padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center;
}
.card-icon { font-size: 2rem; margin-bottom: 0.5rem; }
.card-label { color: #888; font-size: 0.85rem; margin-bottom: 0.25rem; }
.card-value { font-size: 1.8rem; font-weight: 700; color: #1a1a2e; }
.card-sub { color: #aaa; font-size: 0.8rem; margin-top: 0.25rem; }
.status-ok { color: #16a34a; }
.actions {
  display: flex; gap: 1rem; justify-content: center; padding: 1rem 2rem 2rem;
}
.actions button {
  padding: 0.8rem 2rem; border: none; border-radius: 8px;
  font-size: 1rem; cursor: pointer; font-weight: 600;
}
.btn-primary { background: #4f46e5; color: #fff; }
.btn-primary:hover { background: #4338ca; }
.btn-secondary { background: #e0e7ff; color: #4f46e5; }
.btn-secondary:hover { background: #c7d2fe; }
</style>
