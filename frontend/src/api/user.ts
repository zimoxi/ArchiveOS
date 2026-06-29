export async function getMe() {
  const res = await fetch("http://127.0.0.1:8000/api/v1/me")
  return res.json()
}
