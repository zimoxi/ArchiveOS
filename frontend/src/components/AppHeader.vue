<script setup lang="ts">
import { useAppStore } from "../store";

const app = useAppStore();
</script>

<template>
  <header class="app-header">
    <router-link to="/" class="brand">{{ app.projectName }}</router-link>
    <nav>
      <router-link to="/">首页</router-link>
      <router-link to="/dashboard">仪表盘</router-link>
    </nav>
  </header>
</template>

<style scoped>
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 2rem;
  background: #1a1a2e;
  color: #fff;
}
.brand {
  font-weight: 700;
  font-size: 1.2rem;
  color: #fff;
  text-decoration: none;
}
.app-header nav a {
  color: #cbd5e1;
  text-decoration: none;
  margin-left: 1.5rem;
}
.app-header nav a.router-link-active {
  color: #fff;
}
</style>
