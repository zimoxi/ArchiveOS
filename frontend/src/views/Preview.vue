<template>
  <div>
    <h1>Preview</h1>
    <input v-model="file" placeholder="file path"/>
    <button @click="load">Preview</button>
    <pre>{{ result }}</pre>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"

const file = ref("")
const result = ref("")

async function load(){
  const res = await fetch("http://127.0.0.1:8000/api/v1/dashboard")
  result.value = await res.json()
}
</script>
