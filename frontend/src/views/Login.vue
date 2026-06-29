<template>
  <div class="login-page">
    <div class="login-card">
      <h1>OpenFDAMS</h1>
      <p class="subtitle">基金档案管理系统 v2.2</p>
      <form @submit.prevent="doLogin">
        <input v-model="username" type="text" placeholder="用户名" required />
        <input v-model="password" type="password" placeholder="密码 (可留空)" />
        <button type="submit" :disabled="loading">
          {{ loading ? "登录中..." : "登录" }}
        </button>
      </form>
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { useRouter } from "vue-router"
import { login } from "../api/auth"

const router = useRouter()
const username = ref("")
const password = ref("")
const loading = ref(false)
const error = ref("")

async function doLogin() {
  if (!username.value.trim()) { error.value = "请输入用户名"; return }
  loading.value = true
  error.value = ""
  try {
    const data = await login(username.value)
    if (data.access_token) {
      localStorage.setItem("token", data.access_token)
      localStorage.setItem("username", username.value)
      router.push("/dashboard")
    } else {
      error.value = data.detail || "登录失败"
    }
  } catch {
    error.value = "网络错误，请检查后端是否运行"
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh; display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
}
.login-card {
  background: #fff; padding: 3rem 2.5rem; border-radius: 12px;
  text-align: center; width: 380px; box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}
.login-card h1 { color: #1a1a2e; margin-bottom: 0.25rem; font-size: 2rem; }
.subtitle { color: #666; margin-bottom: 2rem; }
.login-card input {
  width: 100%; padding: 0.75rem 1rem; border: 2px solid #e0e0e0;
  border-radius: 8px; font-size: 1rem; margin-bottom: 0.75rem; outline: none;
}
.login-card input:focus { border-color: #4f46e5; }
.login-card button {
  width: 100%; padding: 0.75rem; background: #4f46e5; color: #fff;
  border: none; border-radius: 8px; font-size: 1rem; cursor: pointer;
  font-weight: 600; margin-top: 0.5rem;
}
.login-card button:hover { background: #4338ca; }
.login-card button:disabled { background: #a5a5d0; cursor: not-allowed; }
.error { color: #dc2626; margin-top: 1rem; font-size: 0.9rem; }
</style>
