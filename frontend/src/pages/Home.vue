<script setup lang="ts">
import { useAppStore } from "../store";

const app = useAppStore();
</script>

<template>
  <div class="home">
    <h1>{{ app.projectName }}</h1>
    <p>基金档案管理系统 — v{{ app.version }}</p>
    <nav>
      <router-link to="/dashboard">进入仪表盘</router-link>
    </nav>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 4rem 2rem;
}
.home h1 {
  font-size: 2.5rem;
  color: #1a1a2e;
}
.home p {
  color: #4a4a6a;
  margin-bottom: 2rem;
}
.home nav a {
  color: #4f46e5;
  text-decoration: none;
  font-weight: 600;
}
</style>
