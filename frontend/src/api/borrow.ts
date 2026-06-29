export async function borrowArchive(archiveId: string) {
  const res = await fetch("http://127.0.0.1:8000/api/v1/borrow", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ archive_id: archiveId }),
  })
  return res.json()
}

export async function returnArchive(archiveId: string) {
  const res = await fetch("http://127.0.0.1:8000/api/v1/return", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ archive_id: archiveId }),
  })
  return res.json()
}
