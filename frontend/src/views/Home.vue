<template>
  <div>
    <h1>OpenFDAMS</h1>
    <button @click="load">Test Backend</button>
    <pre>{{ result }}</pre>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { getHealth } from "../api/health"

const result = ref("")

async function load() {
  result.value = await getHealth()
}
</script>
