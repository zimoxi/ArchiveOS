<template>
  <div class="archive-page">
    <header class="topbar">
      <button class="back" @click="$router.push('/dashboard')">← 返回</button>
      <h1>档案管理</h1>
      <span></span>
    </header>

    <div class="content">
      <div class="upload-section">
        <h2>上传档案</h2>
        <div class="upload-box">
          <input type="file" ref="fileInput" @change="onFile" />
          <button @click="doUpload" :disabled="!selectedFile || uploading">
            {{ uploading ? "上传中..." : "上传" }}
          </button>
        </div>
        <p v-if="toast" :class="toast.type === 'ok' ? 'toast-ok' : 'toast-err'">{{ toast.msg }}</p>
      </div>

      <div class="search-bar">
        <input v-model="searchQ" type="text" placeholder="搜索档案..." @keyup.enter="doSearch" />
        <button @click="doSearch">搜索</button>
        <button class="btn-reset" @click="resetSearch">重置</button>
      </div>

      <div class="list-section">
        <h2>档案列表 <span class="count">({{ archives.length }})</span></h2>
        <div v-if="loading" class="empty">加载中...</div>
        <div v-else-if="archives.length === 0" class="empty">
          {{ searchQ ? "无搜索结果" : "暂无档案" }}
        </div>
        <div v-else class="file-list">
          <div v-for="a in archives" :key="a.id" class="file-item">
            <span class="file-icon">📄</span>
            <div class="file-info">
              <span class="file-name">{{ a.title }}</span>
              <span class="file-meta">ID: {{ a.id }} | {{ a.created_at }}</span>
            </div>
            <a v-if="isPreviewable(a.title)" :href="previewUrl(a.id)" target="_blank" class="btn-preview">预览</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue"
import { uploadArchive, getArchiveList, searchArchive, getPreviewUrl } from "../api/archive"

const fileInput = ref<HTMLInputElement | null>(null)
const selectedFile = ref<File | null>(null)
const uploading = ref(false)
const loading = ref(true)
const searchQ = ref("")
const toast = ref<{ type: string; msg: string } | null>(null)
const archives = ref<{ id: number; title: string; file_path: string; created_at: string }[]>([])

onMounted(() => loadArchives())

async function loadArchives(q = "") {
  loading.value = true
  try {
    const data = q ? await searchArchive(q) : await getArchiveList()
    archives.value = Array.isArray(data) ? data : []
  } catch { archives.value = [] }
  finally { loading.value = false }
}

function onFile(e: Event) {
  selectedFile.value = (e.target as HTMLInputElement).files?.[0] || null
  toast.value = null
}

async function doUpload() {
  if (!selectedFile.value) return
  uploading.value = true
  toast.value = null
  try {
    const data = await uploadArchive(selectedFile.value)
    if (data.file_path) {
      toast.value = { type: "ok", msg: `上传成功: ${data.file_name}` }
      selectedFile.value = null
      if (fileInput.value) fileInput.value.value = ""
      await loadArchives()
    } else {
      toast.value = { type: "err", msg: data.detail || "上传失败" }
    }
  } catch { toast.value = { type: "err", msg: "网络错误" } }
  finally { uploading.value = false }
}

function doSearch() { loadArchives(searchQ.value) }
function resetSearch() { searchQ.value = ""; loadArchives() }

function isPreviewable(name: string) {
  const ext = name.split(".").pop()?.toLowerCase() || ""
  return ["pdf", "png", "jpg", "jpeg", "gif", "txt", "md", "csv", "json"].includes(ext)
}
function previewUrl(id: number) { return getPreviewUrl(id) }
</script>

<style scoped>
.archive-page { min-height: 100vh; background: #f0f2f5; }
.topbar {
  background: #1a1a2e; color: #fff; padding: 0.8rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
}
.back {
  background: transparent; border: 1px solid rgba(255,255,255,0.3); color: #fff;
  padding: 0.3rem 0.8rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem;
}
.content { padding: 1.5rem 2rem; max-width: 800px; margin: 0 auto; }
.upload-section, .list-section {
  background: #fff; border-radius: 10px; padding: 1.25rem; margin-bottom: 1rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.upload-section h2, .list-section h2 { margin-bottom: 0.75rem; font-size: 1.1rem; }
.count { color: #888; font-weight: normal; font-size: 0.85rem; }
.upload-box { display: flex; gap: 0.75rem; align-items: center; }
.upload-box input { flex: 1; }
.upload-box button {
  padding: 0.5rem 1.2rem; background: #4f46e5; color: #fff;
  border: none; border-radius: 6px; cursor: pointer; white-space: nowrap;
}
.upload-box button:disabled { background: #a5a5d0; cursor: not-allowed; }
.toast-ok { color: #16a34a; margin-top: 0.5rem; font-size: 0.9rem; }
.toast-err { color: #dc2626; margin-top: 0.5rem; font-size: 0.9rem; }
.search-bar {
  display: flex; gap: 0.5rem; margin-bottom: 1rem;
}
.search-bar input {
  flex: 1; padding: 0.5rem 0.75rem; border: 2px solid #e0e0e0;
  border-radius: 6px; font-size: 0.9rem; outline: none;
}
.search-bar input:focus { border-color: #4f46e5; }
.search-bar button {
  padding: 0.5rem 1rem; border: none; border-radius: 6px;
  cursor: pointer; font-size: 0.85rem;
}
.search-bar button:first-of-type { background: #4f46e5; color: #fff; }
.btn-reset { background: #e0e7ff; color: #4f46e5; }
.empty { color: #999; text-align: center; padding: 2rem; }
.file-list { display: flex; flex-direction: column; gap: 0.5rem; }
.file-item {
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.65rem; background: #f8f9fa; border-radius: 8px;
}
.file-icon { font-size: 1.1rem; }
.file-info { display: flex; flex-direction: column; flex: 1; }
.file-name { font-weight: 600; font-size: 0.9rem; }
.file-meta { color: #888; font-size: 0.75rem; }
.btn-preview {
  padding: 0.3rem 0.7rem; background: #e0e7ff; color: #4f46e5;
  border-radius: 4px; text-decoration: none; font-size: 0.8rem; font-weight: 600;
}
.btn-preview:hover { background: #c7d2fe; }
</style>
