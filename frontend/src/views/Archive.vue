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
        <div class="form-grid">
          <input v-model="form.title" type="text" placeholder="档案标题" />
          <input v-model="form.category" type="text" placeholder="分类 (如: 合同/报告/函件)" />
          <input v-model="form.description" type="text" placeholder="描述 (可选)" class="full" />
          <div class="upload-row full">
            <input type="file" ref="fileInput" @change="onFile" />
            <button @click="doUpload" :disabled="!selectedFile || uploading">
              {{ uploading ? "上传中..." : "上传" }}
            </button>
          </div>
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
        <div v-else class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>标题</th>
                <th>分类</th>
                <th>描述</th>
                <th>文件</th>
                <th>创建时间</th>
                <th>操作</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="a in archives" :key="a.id">
                <td>{{ a.id }}</td>
                <td class="td-title">{{ a.title }}</td>
                <td><span class="tag-cat">{{ a.category || "—" }}</span></td>
                <td class="td-desc">{{ a.description || "—" }}</td>
                <td class="td-path">{{ shortPath(a.file_path) }}</td>
                <td class="td-time">{{ a.created_at }}</td>
                <td>
                  <a v-if="isPreviewable(a.title)" :href="previewUrl(a.id)" target="_blank" class="btn-preview">预览</a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from "vue"
import { getArchiveList, searchArchive, getPreviewUrl } from "../api/archive"

const fileInput = ref<HTMLInputElement | null>(null)
const selectedFile = ref<File | null>(null)
const uploading = ref(false)
const loading = ref(true)
const searchQ = ref("")
const toast = ref<{ type: string; msg: string } | null>(null)
const form = reactive({ title: "", description: "", category: "" })
const archives = ref<{
  id: number; title: string; description: string; category: string;
  file_path: string; created_by: number; created_at: string
}[]>([])

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
  if (selectedFile.value && !form.title) {
    form.title = selectedFile.value.name
  }
}

async function doUpload() {
  if (!selectedFile.value) return
  uploading.value = true; toast.value = null
  try {
    const fd = new FormData()
    fd.append("file", selectedFile.value)
    if (form.title) fd.append("title", form.title)
    if (form.description) fd.append("description", form.description)
    if (form.category) fd.append("category", form.category)

    const token = localStorage.getItem("token") || ""
    const res = await fetch("http://127.0.0.1:8010/api/v1/upload", {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` },
      body: fd,
    })
    const data = await res.json()

    if (data.id) {
      toast.value = { type: "ok", msg: `上传成功: ${data.title}` }
      form.title = ""; form.description = ""; form.category = ""
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
function shortPath(p: string) { return p ? p.split(/[/\\]/).pop() || p : "—" }
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
.content { padding: 1.5rem 2rem; max-width: 1000px; margin: 0 auto; }
.upload-section, .list-section {
  background: #fff; border-radius: 10px; padding: 1.25rem; margin-bottom: 1rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.upload-section h2, .list-section h2 { margin-bottom: 0.75rem; font-size: 1.1rem; }
.count { color: #888; font-weight: normal; font-size: 0.85rem; }
.form-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 0.6rem;
}
.form-grid input {
  padding: 0.5rem 0.75rem; border: 2px solid #e0e0e0;
  border-radius: 6px; font-size: 0.9rem; outline: none;
}
.form-grid input:focus { border-color: #4f46e5; }
.full { grid-column: 1 / -1; }
.upload-row { display: flex; gap: 0.75rem; align-items: center; }
.upload-row input { flex: 1; border: none; padding: 0; }
.upload-row button {
  padding: 0.5rem 1.2rem; background: #4f46e5; color: #fff;
  border: none; border-radius: 6px; cursor: pointer; white-space: nowrap;
}
.upload-row button:disabled { background: #a5a5d0; cursor: not-allowed; }
.toast-ok { color: #16a34a; margin-top: 0.5rem; font-size: 0.9rem; }
.toast-err { color: #dc2626; margin-top: 0.5rem; font-size: 0.9rem; }
.search-bar { display: flex; gap: 0.5rem; margin-bottom: 1rem; }
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
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
th { background: #f8f9fa; text-align: left; padding: 0.5rem 0.6rem; font-weight: 600; color: #555; border-bottom: 2px solid #e5e7eb; }
td { padding: 0.5rem 0.6rem; border-bottom: 1px solid #f0f0f0; vertical-align: top; }
.td-title { font-weight: 600; }
.td-desc { color: #666; max-width: 180px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.td-path { color: #888; font-size: 0.8rem; }
.td-time { color: #888; font-size: 0.8rem; white-space: nowrap; }
.tag-cat {
  background: #e0e7ff; color: #4f46e5; padding: 0.1rem 0.4rem;
  border-radius: 3px; font-size: 0.75rem;
}
.btn-preview {
  padding: 0.2rem 0.5rem; background: #e0e7ff; color: #4f46e5;
  border-radius: 4px; text-decoration: none; font-size: 0.75rem; font-weight: 600;
}
.btn-preview:hover { background: #c7d2fe; }
</style>
