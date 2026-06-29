<template>
  <div>
    <h1>Dashboard</h1>
    <button @click="load">Load Stats</button>
    <pre>{{ data }}</pre>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"

const data = ref("")

async function load(){
  const res = await fetch("http://127.0.0.1:8000/api/v1/dashboard")
  data.value = await res.json()
}
</script>
