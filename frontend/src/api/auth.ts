import { request } from "./http"

export async function login(username: string) {
  const res = await fetch("http://127.0.0.1:8020/api/v1/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username }),
  })
  return res.json()
}

export async function getMe() {
  return request("http://127.0.0.1:8020/api/v1/me")
}
