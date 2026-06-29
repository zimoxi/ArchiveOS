export async function login(username: string) {
  const res = await fetch("http://127.0.0.1:8000/api/v1/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username }),
  })
  return res.json()
}

export async function getMe() {
  const res = await fetch("http://127.0.0.1:8000/api/v1/me")
  return res.json()
}
