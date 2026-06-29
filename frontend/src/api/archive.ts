import { request } from "./http"

export async function uploadArchive(file: File) {
  const form = new FormData()
  form.append("file", file)
  const res = await fetch("http://127.0.0.1:8000/api/v1/upload", {
    method: "POST",
    body: form,
  })
  return res.json()
}

export async function getDashboard() {
  return request("http://127.0.0.1:8000/api/v1/dashboard")
}
