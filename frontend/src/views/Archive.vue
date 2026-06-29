<template>
  <div>
    <h1>Archive Upload</h1>
    <input type="file" @change="onFile"/>
    <button @click="upload">Upload</button>
    <pre>{{ result }}</pre>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue"

const file = ref(null)
const result = ref("")

function onFile(e:any){
  file.value = e.target.files[0]
}

async function upload(){
  const form = new FormData()
  form.append("file", file.value)

  const res = await fetch("http://127.0.0.1:8000/api/v1/upload", {
    method: "POST",
    body: form
  })

  result.value = await res.json()
}
</script>
