export async function request(url: string) {
  const res = await fetch(url)
  return res.json()
}
