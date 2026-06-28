# LINUX_DOCKER_COMPATIBILITY_STANDARD

## 目标

即使当前在 Windows 开发，代码也必须能在未来 Linux Docker 中运行。

## 要求

- 不写 Windows 专属路径
- 不依赖 Windows 服务
- 文件路径使用 pathlib
- 环境变量统一
- 本地启动与 Docker 启动使用同一入口
- 依赖写入 requirements.txt / package.json

## 禁止

```text
C:\
D:\
win32api
绝对路径
真实密钥
```
