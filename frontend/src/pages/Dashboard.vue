<script setup lang="ts">
import { ref, onMounted } from "vue";

const healthStatus = ref("checking...");

onMounted(async () => {
  try {
    const res = await fetch("/api/health");
    const data = await res.json();
    healthStatus.value = data.status;
  } catch {
    healthStatus.value = "unreachable";
  }
});
</script>

<template>
  <div class="dashboard">
    <h1>Dashboard</h1>
    <div class="card">
      <h3>Backend Status</h3>
      <span :class="healthStatus === 'ok' ? 'badge-ok' : 'badge-err'">
        {{ healthStatus }}
      </span>
    </div>
    <nav>
      <router-link to="/">← 返回首页</router-link>
    </nav>
  </div>
</template>

<style scoped>
.dashboard {
  padding: 2rem;
}
.card {
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1.5rem;
  max-width: 400px;
  margin: 1rem auto;
}
.badge-ok {
  color: #16a34a;
  font-weight: bold;
}
.badge-err {
  color: #dc2626;
  font-weight: bold;
}
.dashboard nav {
  text-align: center;
  margin-top: 2rem;
}
.dashboard nav a {
  color: #4f46e5;
}
</style>
