<template>
  <div class="dashboard">
    <header class="topbar">
      <h1>OpenFDAMS <span class="ver">v2.2</span></h1>
      <div class="nav">
        <router-link to="/archive">档案</router-link>
        <router-link to="/borrow">借阅</router-link>
        <router-link to="/search">搜索</router-link>
        <router-link to="/logs">日志</router-link>
      </div>
      <div class="user-info">
        <span>{{ user.username }}</span>
        <span class="role">{{ user.role }}</span>
        <button @click="logout">退出</button>
      </div>
    </header>

    <div v-if="loading" class="loading">加载中...</div>
    <div v-else-if="error" class="error-banner">{{ error }}</div>
    <template v-else>
      <div class="cards">
        <div class="card"><div class="card-icon">📁</div><div class="card-label">档案总数</div><div class="card-value">{{ stats.archives }}</div></div>
        <div class="card"><div class="card-icon">📋</div><div class="card-label">借阅中</div><div class="card-value">{{ stats.borrows_active }}</div></div>
        <div class="card"><div class="card-icon">📊</div><div class="card-label">借阅总量</div><div class="card-value">{{ stats.borrows_total }}</div></div>
        <div class="card"><div class="card-icon">👥</div><div class="card-label">用户数</div><div class="card-value">{{ stats.users }}</div></div>
        <div class="card"><div class="card-icon">📤</div><div class="card-label">今日上传</div><div class="card-value">{{ stats.uploads_today }}</div></div>
        <div class="card"><div class="card-icon">📝</div><div class="card-label">操作日志</div><div class="card-value">{{ stats.logs }}</div></div>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"
import { getDashboard } from "../api/archive"

const router = useRouter()
const loading = ref(true)
const error = ref("")
const user = ref({ id: 0, username: "", role: "" })
const stats = ref({ users: 0, archives: 0, borrows_active: 0, borrows_total: 0, uploads_today: 0, logs: 0 })

onMounted(async () => {
  try {
    const data = await getDashboard()
    if (data.user) user.value = data.user
    if (data.stats) stats.value = data.stats
  } catch {
    error.value = "加载失败"
  } finally {
    loading.value = false
  }
})

function logout() {
  localStorage.removeItem("token")
  localStorage.removeItem("username")
  router.push("/login")
}
</script>

<style scoped>
.dashboard { min-height: 100vh; background: #f0f2f5; }
.topbar {
  background: #1a1a2e; color: #fff; padding: 0.8rem 2rem;
  display: flex; align-items: center; gap: 2rem;
}
.topbar h1 { font-size: 1.3rem; white-space: nowrap; }
.ver { font-size: 0.75rem; color: #8b8ba0; font-weight: normal; }
.nav { display: flex; gap: 1rem; }
.nav a { color: #a0a0c0; text-decoration: none; font-size: 0.9rem; padding: 0.3rem 0.6rem; border-radius: 6px; }
.nav a:hover, .nav a.router-link-active { color: #fff; background: rgba(255,255,255,0.1); }
.user-info { margin-left: auto; display: flex; align-items: center; gap: 0.75rem; }
.role { background: #4f46e5; padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.75rem; }
.user-info button {
  background: transparent; border: 1px solid rgba(255,255,255,0.3); color: #fff;
  padding: 0.3rem 0.8rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem;
}
.loading { text-align: center; padding: 4rem; color: #888; font-size: 1.1rem; }
.error-banner { background: #fef2f2; color: #dc2626; padding: 1rem 2rem; text-align: center; }
.cards {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1.25rem; padding: 2rem;
}
.card {
  background: #fff; border-radius: 12px; padding: 1.25rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06); text-align: center;
}
.card-icon { font-size: 1.8rem; margin-bottom: 0.4rem; }
.card-label { color: #888; font-size: 0.8rem; margin-bottom: 0.2rem; }
.card-value { font-size: 1.6rem; font-weight: 700; color: #1a1a2e; }
</style>
