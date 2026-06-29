import { request } from "./http"

export async function borrowArchive(archiveId: number) {
  return request("http://127.0.0.1:8020/api/v1/borrow", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ archive_id: archiveId }),
  })
}

export async function returnArchive(archiveId: number) {
  return request("http://127.0.0.1:8020/api/v1/return", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ archive_id: archiveId }),
  })
}

export async function getBorrowHistory() {
  return request("http://127.0.0.1:8020/api/v1/borrow/history")
}

export async function searchBorrow(q: string) {
  return request(`http://127.0.0.1:8020/api/v1/search/borrow?q=${encodeURIComponent(q)}`)
}
