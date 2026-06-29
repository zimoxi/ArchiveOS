<template>
  <div class="search-page">
    <header class="topbar">
      <button class="back" @click="$router.push('/dashboard')">← 返回</button>
      <h1>统一搜索</h1>
      <span></span>
    </header>

    <div class="content">
      <div class="search-bar">
        <input v-model="q" type="text" placeholder="输入关键词搜索档案和借阅记录..." @keyup.enter="doSearch" autofocus />
        <button @click="doSearch" :disabled="!q.trim()">搜索</button>
      </div>

      <div v-if="searched">
        <div class="result-section">
          <h3>📁 档案结果 <span class="count">({{ archiveResults.length }})</span></h3>
          <div v-if="archiveResults.length === 0" class="empty">无档案结果</div>
          <div v-else class="file-list">
            <div v-for="a in archiveResults" :key="a.id" class="file-item">
              <span class="file-icon">📄</span>
              <div class="file-info">
                <span class="file-name">{{ a.title }}</span>
                <span class="file-meta">ID: {{ a.id }} | {{ a.created_at }}</span>
              </div>
            </div>
          </div>
        </div>

        <div class="result-section">
          <h3>📋 借阅结果 <span class="count">({{ borrowResults.length }})</span></h3>
          <div v-if="borrowResults.length === 0" class="empty">无借阅结果</div>
          <div v-else class="file-list">
            <div v-for="b in borrowResults" :key="b.id" class="file-item">
              <span class="tag" :class="b.status === 'returned' ? 'tag-returned' : 'tag-active'">
                {{ b.status === "returned" ? "已归还" : "借阅中" }}
              </span>
              <div class="file-info">
                <span class="file-name">档案 #{{ b.archive_id }}</span>
                <span class="file-meta">{{ b.created_at }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="hint">输入关键词开始搜索</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { searchArchive } from "../api/archive"
import { searchBorrow } from "../api/borrow"

const q = ref("")
const searched = ref(false)
const archiveResults = ref<{ id: number; title: string; created_at: string }[]>([])
const borrowResults = ref<{ id: number; archive_id: number; status: string; created_at: string }[]>([])

async function doSearch() {
  if (!q.value.trim()) return
  searched.value = true
  try {
    const [a, b] = await Promise.all([searchArchive(q.value), searchBorrow(q.value)])
    archiveResults.value = Array.isArray(a) ? a : []
    borrowResults.value = Array.isArray(b) ? b : []
  } catch {
    archiveResults.value = []
    borrowResults.value = []
  }
}
</script>

<style scoped>
.search-page { min-height: 100vh; background: #f0f2f5; }
.topbar {
  background: #1a1a2e; color: #fff; padding: 0.8rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
}
.back {
  background: transparent; border: 1px solid rgba(255,255,255,0.3); color: #fff;
  padding: 0.3rem 0.8rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem;
}
.content { padding: 1.5rem 2rem; max-width: 800px; margin: 0 auto; }
.search-bar { display: flex; gap: 0.5rem; margin-bottom: 1.5rem; }
.search-bar input {
  flex: 1; padding: 0.65rem 1rem; border: 2px solid #e0e0e0;
  border-radius: 8px; font-size: 1rem; outline: none;
}
.search-bar input:focus { border-color: #4f46e5; }
.search-bar button {
  padding: 0.65rem 1.5rem; background: #4f46e5; color: #fff;
  border: none; border-radius: 8px; cursor: pointer; font-weight: 600;
}
.search-bar button:disabled { background: #a5a5d0; cursor: not-allowed; }
.result-section {
  background: #fff; border-radius: 10px; padding: 1.25rem; margin-bottom: 1rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.result-section h3 { margin-bottom: 0.75rem; font-size: 1rem; }
.count { color: #888; font-weight: normal; font-size: 0.85rem; }
.empty { color: #999; text-align: center; padding: 1rem; }
.hint { color: #999; text-align: center; padding: 3rem; font-size: 1rem; }
.file-list { display: flex; flex-direction: column; gap: 0.4rem; }
.file-item {
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.5rem; background: #f8f9fa; border-radius: 6px;
}
.file-icon { font-size: 1.1rem; }
.file-info { display: flex; flex-direction: column; }
.file-name { font-weight: 600; font-size: 0.9rem; }
.file-meta { color: #888; font-size: 0.75rem; }
.tag {
  padding: 0.15rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: 600;
}
.tag-active { background: #e0e7ff; color: #4f46e5; }
.tag-returned { background: #f0fdf4; color: #16a34a; }
</style>
