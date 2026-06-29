export function getToken(): string {
  return localStorage.getItem("token") || ""
}

export async function request(url: string, options: RequestInit = {}) {
  const token = getToken()
  const headers: Record<string, string> = {
    ...((options.headers as Record<string, string>) || {}),
  }
  if (token) headers["Authorization"] = `Bearer ${token}`

  const res = await fetch(url, { ...options, headers })
  if (res.status === 401 || res.status === 403) {
    localStorage.removeItem("token")
    localStorage.removeItem("username")
    window.location.href = "/login"
    throw new Error("Unauthorized")
  }
  return res.json()
}
