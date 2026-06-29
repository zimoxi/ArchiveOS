import { request } from "./http"

export async function uploadArchive(file: File) {
  const token = localStorage.getItem("token") || ""
  const form = new FormData()
  form.append("file", file)
  const res = await fetch("http://127.0.0.1:8010/api/v1/upload", {
    method: "POST",
    headers: { Authorization: `Bearer ${token}` },
    body: form,
  })
  return res.json()
}

export async function getArchiveList() {
  return request("http://127.0.0.1:8010/api/v1/archive/list")
}

export async function searchArchive(q: string) {
  return request(`http://127.0.0.1:8010/api/v1/search/archive?q=${encodeURIComponent(q)}`)
}

export async function getDashboard() {
  return request("http://127.0.0.1:8010/api/v1/stats/dashboard")
}

export function getPreviewUrl(archiveId: number) {
  return `http://127.0.0.1:8010/api/v1/preview/${archiveId}`
}
