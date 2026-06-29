<template>
  <div>
    <h1>Borrow System</h1>
    <button @click="borrow">Borrow</button>
    <button @click="ret">Return</button>
    <pre>{{ result }}</pre>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"

const result = ref("")

async function borrow(){
  const res = await fetch("http://127.0.0.1:8000/api/v1/borrow", {method:"POST"})
  result.value = await res.json()
}

async function ret(){
  const res = await fetch("http://127.0.0.1:8000/api/v1/return", {method:"POST"})
  result.value = await res.json()
}
</script>
