import { request } from "./http"

export async function getLogs() {
  return request("http://127.0.0.1:8020/api/v1/logs")
}
