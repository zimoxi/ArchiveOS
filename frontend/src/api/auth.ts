export async function login() {
  const res = await fetch("http://127.0.0.1:8000/api/v1/login", {
    method: "POST"
  })
  return res.json()
}
