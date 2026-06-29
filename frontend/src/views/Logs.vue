<template>
  <div class="logs-page">
    <header class="topbar">
      <button class="back" @click="$router.push('/dashboard')">← 返回</button>
      <h1>操作日志</h1>
      <button class="btn-refresh" @click="loadLogs">刷新</button>
    </header>

    <div class="content">
      <div v-if="loading" class="empty">加载中...</div>
      <div v-else-if="logs.length === 0" class="empty">暂无操作日志</div>
      <div v-else class="log-list">
        <div v-for="log in logs" :key="log.id" class="log-item">
          <span class="log-action">{{ log.action }}</span>
          <span class="log-target">{{ log.target }}</span>
          <span class="log-meta">用户 #{{ log.user_id }}</span>
          <span class="log-time">{{ log.created_at }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import { getLogs } from "../api/logs"

const loading = ref(true)
const logs = ref<{ id: number; user_id: number; action: string; target: string; created_at: string }[]>([])

onMounted(() => loadLogs())

async function loadLogs() {
  loading.value = true
  try {
    const data = await getLogs()
    logs.value = Array.isArray(data) ? data : []
  } catch { logs.value = [] }
  finally { loading.value = false }
}
</script>

<style scoped>
.logs-page { min-height: 100vh; background: #f0f2f5; }
.topbar {
  background: #1a1a2e; color: #fff; padding: 0.8rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
}
.back {
  background: transparent; border: 1px solid rgba(255,255,255,0.3); color: #fff;
  padding: 0.3rem 0.8rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem;
}
.btn-refresh {
  background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.3);
  color: #fff; padding: 0.3rem 0.8rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem;
}
.content { padding: 1.5rem 2rem; max-width: 800px; margin: 0 auto; }
.empty { color: #999; text-align: center; padding: 3rem; }
.log-list { display: flex; flex-direction: column; gap: 0.4rem; }
.log-item {
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.6rem 0.75rem; background: #fff; border-radius: 6px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04);
}
.log-action {
  background: #e0e7ff; color: #4f46e5; padding: 0.15rem 0.5rem;
  border-radius: 4px; font-size: 0.75rem; font-weight: 600; white-space: nowrap;
}
.log-target { font-weight: 500; font-size: 0.9rem; }
.log-meta { color: #888; font-size: 0.8rem; }
.log-time { color: #aaa; font-size: 0.75rem; margin-left: auto; white-space: nowrap; }
</style>
