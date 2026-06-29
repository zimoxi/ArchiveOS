<template>
  <div>
    <h1>Login</h1>
    <button @click="doLogin">Login</button>
    <pre>{{ result }}</pre>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"
import { login } from "../api/auth"

const result = ref("")

async function doLogin(){
  result.value = await login()
}
</script>
