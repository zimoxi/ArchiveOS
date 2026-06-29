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
          <input v-model="archiveId" type="text" placeholder="输入档案 ID" />
          <button class="btn-borrow" @click="doBorrow" :disabled="!archiveId || loading">
            {{ loading ? "处理中..." : "借阅" }}
          </button>
          <button class="btn-return" @click="doReturn" :disabled="!archiveId || loading">
            归还
          </button>
        </div>
      </div>

      <div v-if="result" class="result-section">
        <h2>操作结果</h2>
        <div class="result-card" :class="result.ok ? 'result-ok' : 'result-err'">
          <div class="result-icon">{{ result.ok ? "✅" : "❌" }}</div>
          <div class="result-msg">{{ result.message }}</div>
          <div v-if="result.detail" class="result-detail">{{ result.detail }}</div>
        </div>
      </div>

      <div class="history-section">
        <h2>操作历史</h2>
        <div v-if="history.length === 0" class="empty">暂无记录</div>
        <div v-else class="history-list">
          <div v-for="(h, i) in history" :key="i" class="history-item">
            <span class="history-action" :class="h.action === '借阅' ? 'tag-borrow' : 'tag-return'">
              {{ h.action }}
            </span>
            <span class="history-id">档案 {{ h.archiveId }}</span>
            <span class="history-status">{{ h.message }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { borrowArchive, returnArchive } from "../api/borrow"

const archiveId = ref("")
const loading = ref(false)
const result = ref<{ ok: boolean; message: string; detail?: string } | null>(null)
const history = ref<{ action: string; archiveId: string; message: string }[]>([])

async function doBorrow() {
  if (!archiveId.value) return
  loading.value = true
  try {
    const data = await borrowArchive(archiveId.value)
    const ok = !data.detail
    result.value = {
      ok,
      message: ok ? "借阅成功" : "借阅失败",
      detail: JSON.stringify(data),
    }
    history.value.unshift({
      action: "借阅",
      archiveId: archiveId.value,
      message: ok ? "成功" : data.detail || "失败",
    })
  } catch {
    result.value = { ok: false, message: "网络错误" }
  } finally {
    loading.value = false
  }
}

async function doReturn() {
  if (!archiveId.value) return
  loading.value = true
  try {
    const data = await returnArchive(archiveId.value)
    const ok = !data.detail
    result.value = {
      ok,
      message: ok ? "归还成功" : "归还失败",
      detail: JSON.stringify(data),
    }
    history.value.unshift({
      action: "归还",
      archiveId: archiveId.value,
      message: ok ? "成功" : data.detail || "失败",
    })
  } catch {
    result.value = { ok: false, message: "网络错误" }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.borrow-page { min-height: 100vh; background: #f5f5f5; }
.topbar {
  background: #1a1a2e; color: #fff; padding: 1rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
}
.back {
  background: transparent; border: 1px solid #fff; color: #fff;
  padding: 0.4rem 1rem; border-radius: 6px; cursor: pointer;
}
.content { padding: 2rem; max-width: 700px; margin: 0 auto; }
.section, .result-section, .history-section {
  background: #fff; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.section h2, .result-section h2, .history-section h2 {
  margin-bottom: 1rem; font-size: 1.2rem;
}
.form-row { display: flex; gap: 0.75rem; align-items: center; }
.form-row input {
  flex: 1; padding: 0.6rem 1rem; border: 2px solid #e0e0e0;
  border-radius: 8px; font-size: 1rem; outline: none;
}
.form-row input:focus { border-color: #4f46e5; }
.btn-borrow, .btn-return {
  padding: 0.6rem 1.5rem; border: none; border-radius: 8px;
  cursor: pointer; font-weight: 600; white-space: nowrap;
}
.btn-borrow { background: #4f46e5; color: #fff; }
.btn-borrow:disabled { background: #a5a5d0; cursor: not-allowed; }
.btn-return { background: #e0e7ff; color: #4f46e5; }
.btn-return:disabled { background: #f0f0f0; color: #999; cursor: not-allowed; }
.result-card {
  padding: 1rem; border-radius: 8px; display: flex; align-items: center; gap: 1rem;
}
.result-ok { background: #f0fdf4; border: 1px solid #bbf7d0; }
.result-err { background: #fef2f2; border: 1px solid #fecaca; }
.result-icon { font-size: 1.5rem; }
.result-msg { font-weight: 600; }
.result-detail { color: #666; font-size: 0.85rem; margin-left: auto; }
.empty { color: #999; text-align: center; padding: 1.5rem; }
.history-list { display: flex; flex-direction: column; gap: 0.5rem; }
.history-item {
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.6rem; background: #f8f9fa; border-radius: 8px;
}
.history-action {
  padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.8rem; font-weight: 600;
}
.tag-borrow { background: #e0e7ff; color: #4f46e5; }
.tag-return { background: #f0fdf4; color: #16a34a; }
.history-id { font-weight: 600; }
.history-status { color: #666; margin-left: auto; font-size: 0.9rem; }
</style>
