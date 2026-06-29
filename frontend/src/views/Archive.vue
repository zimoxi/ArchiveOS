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
            {{ uploading ? "上传中..." : "上传文件" }}
          </button>
        </div>
        <p v-if="uploadResult" class="upload-ok">✅ 上传成功: {{ uploadResult }}</p>
        <p v-if="uploadError" class="upload-err">{{ uploadError }}</p>
      </div>

      <div class="list-section">
        <h2>已上传文件</h2>
        <div v-if="files.length === 0" class="empty">暂无文件</div>
        <div v-else class="file-list">
          <div v-for="(f, i) in files" :key="i" class="file-item">
            <span class="file-icon">📄</span>
            <span class="file-name">{{ f.name }}</span>
            <span class="file-path">{{ f.path }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { uploadArchive } from "../api/archive"

const fileInput = ref<HTMLInputElement | null>(null)
const selectedFile = ref<File | null>(null)
const uploading = ref(false)
const uploadResult = ref("")
const uploadError = ref("")
const files = ref<{ name: string; path: string }[]>([])

function onFile(e: Event) {
  const input = e.target as HTMLInputElement
  selectedFile.value = input.files?.[0] || null
  uploadResult.value = ""
  uploadError.value = ""
}

async function doUpload() {
  if (!selectedFile.value) return
  uploading.value = true
  uploadError.value = ""
  try {
    const data = await uploadArchive(selectedFile.value)
    if (data.file_path) {
      uploadResult.value = data.file_path
      files.value.unshift({ name: selectedFile.value.name, path: data.file_path })
      selectedFile.value = null
      if (fileInput.value) fileInput.value.value = ""
    } else {
      uploadError.value = "上传失败"
    }
  } catch {
    uploadError.value = "网络错误"
  } finally {
    uploading.value = false
  }
}
</script>

<style scoped>
.archive-page { min-height: 100vh; background: #f5f5f5; }
.topbar {
  background: #1a1a2e; color: #fff; padding: 1rem 2rem;
  display: flex; align-items: center; justify-content: space-between;
}
.back {
  background: transparent; border: 1px solid #fff; color: #fff;
  padding: 0.4rem 1rem; border-radius: 6px; cursor: pointer;
}
.content { padding: 2rem; max-width: 800px; margin: 0 auto; }
.upload-section, .list-section {
  background: #fff; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.upload-section h2, .list-section h2 { margin-bottom: 1rem; font-size: 1.2rem; }
.upload-box { display: flex; gap: 1rem; align-items: center; }
.upload-box input { flex: 1; }
.upload-box button {
  padding: 0.6rem 1.5rem; background: #4f46e5; color: #fff;
  border: none; border-radius: 8px; cursor: pointer; white-space: nowrap;
}
.upload-box button:disabled { background: #a5a5d0; cursor: not-allowed; }
.upload-ok { color: #16a34a; margin-top: 0.75rem; }
.upload-err { color: #dc2626; margin-top: 0.75rem; }
.empty { color: #999; text-align: center; padding: 2rem; }
.file-list { display: flex; flex-direction: column; gap: 0.5rem; }
.file-item {
  display: flex; align-items: center; gap: 0.75rem;
  padding: 0.75rem; background: #f8f9fa; border-radius: 8px;
}
.file-icon { font-size: 1.2rem; }
.file-name { font-weight: 600; }
.file-path { color: #888; font-size: 0.85rem; margin-left: auto; }
</style>
