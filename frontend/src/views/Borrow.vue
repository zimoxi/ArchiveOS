<template>
  <div class="borrow-page">
    <header class="topbar">
      <button class="back" @click="$router.push('/dashboard')">← 返回</button>
      <h1>借阅管理</h1>
      <span></span>
    </header>

    <div class="content">
      <div class="section">
        <h2>借阅操作</h2>
        <div class="form-row">
          <input v-model="archiveId" type="number" placeholder="档案 ID" />
          <button class="btn-borrow" @click="doBorrow" :disabled="!archiveId || loading">
            {{ loading ? "处理中..." : "借阅" }}
          </button>
          <button class="btn-return" @click="doReturn" :disabled="!archiveId || loading">归还</button>
        </div>
        <p v-if="toast" :class="toast.type === 'ok' ? 'toast-ok' : 'toast-err'">{{ toast.msg }}</p>
      </div>

      <div class="history-section">
        <h2>借阅记录 <span class="count">({{ history.length }})</span></h2>
        <div v-if="historyLoading" class="empty">加载中...</div>
        <div v-else-if="history.length === 0" class="empty">暂无借阅记录</div>
        <div v-else class="history-list">
          <div v-for="h in history" :key="h.id" class="history-item">
            <span class="history-tag" :class="h.status === 'returned' ? 'tag-returned' : 'tag-active'">
              {{ h.status === "returned" ? "已归还" : "借阅中" }}
            </span>
            <span class="history-id">档案 #{{ h.archive_id }}</span>
            <span class="history-date">{{ h.created_at }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import { borrowArchive, returnArchive, getBorrowHistory } from "../api/borrow"

const archiveId = ref<number | null>(null)
const loading = ref(false)
const historyLoading = ref(true)
const toast = ref<{ type: string; msg: string } | null>(null)
const history = ref<{ id: number; archive_id: number; status: string; created_at: string }[]>([])

onMounted(() => loadHistory())

async function loadHistory() {
  historyLoading.value = true
  try {
    const data = await getBorrowHistory()
    history.value = Array.isArray(data) ? data : []
  } catch { history.value = [] }
  finally { historyLoading.value = false }
}

async function doBorrow() {
  if (!archiveId.value) return
  loading.value = true; toast.value = null
  try {
    const data = await borrowArchive(archiveId.value)
    if (data.id) { toast.value = { type: "ok", msg: `借阅成功 #${data.id}` }; await loadHistory() }
    else { toast.value = { type: "err", msg: data.detail || "借阅失败" } }
  } catch { toast.value = { type: "err", msg: "网络错误" } }
  finally { loading.value = false }
}

async function doReturn() {
  if (!archiveId.value) return
  loading.value = true; toast.value = null
  try {
    const data = await returnArchive(archiveId.value)
    if (data.status === "returned") { toast.value = { type: "ok", msg: "归还成功" }; await loadHistory() }
    else { toast.value = { type: "err", msg: data.detail || "归还失败" } }
  } catch { toast.value = { type: "err", msg: "网络错误" } }
  finally { loading.value = false }
}
</script>

<style scoped>
.borrow-page { min-height: 100vh; background: #f0f2f5; }
.topbar {
  background: #1a1a2e; color: #fff; padding: 0.8rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
}
.back {
  background: transparent; border: 1px solid rgba(255,255,255,0.3); color: #fff;
  padding: 0.3rem 0.8rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem;
}
.content { padding: 1.5rem 2rem; max-width: 700px; margin: 0 auto; }
.section, .history-section {
  background: #fff; border-radius: 10px; padding: 1.25rem; margin-bottom: 1rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.section h2, .history-section h2 { margin-bottom: 0.75rem; font-size: 1.1rem; }
.count { color: #888; font-weight: normal; font-size: 0.85rem; }
.form-row { display: flex; gap: 0.5rem; align-items: center; }
.form-row input {
  flex: 1; padding: 0.5rem 0.75rem; border: 2px solid #e0e0e0;
  border-radius: 6px; font-size: 0.9rem; outline: none;
}
.form-row input:focus { border-color: #4f46e5; }
.btn-borrow, .btn-return {
  padding: 0.5rem 1.2rem; border: none; border-radius: 6px;
  cursor: pointer; font-weight: 600; font-size: 0.85rem;
}
.btn-borrow { background: #4f46e5; color: #fff; }
.btn-borrow:disabled { background: #a5a5d0; cursor: not-allowed; }
.btn-return { background: #e0e7ff; color: #4f46e5; }
.btn-return:disabled { background: #f0f0f0; color: #999; cursor: not-allowed; }
.toast-ok { color: #16a34a; margin-top: 0.5rem; font-size: 0.9rem; }
.toast-err { color: #dc2626; margin-top: 0.5rem; font-size: 0.9rem; }
.empty { color: #999; text-align: center; padding: 1.5rem; }
.history-list { display: flex; flex-direction: column; gap: 0.4rem; }
.history-item {
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.5rem; background: #f8f9fa; border-radius: 6px;
}
.history-tag {
  padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600;
}
.tag-active { background: #e0e7ff; color: #4f46e5; }
.tag-returned { background: #f0fdf4; color: #16a34a; }
.history-id { font-weight: 600; font-size: 0.9rem; }
.history-date { color: #888; margin-left: auto; font-size: 0.8rem; }
</style>
