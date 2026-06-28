# CURRENT_CONTEXT

## 当前开发环境

```text
OS: Windows 11
Shell: PowerShell / CMD
Python: 3.12
Node.js: LTS
Frontend: Vue 3 + Vite + TypeScript
Backend: FastAPI
Database: PostgreSQL（后续）
Cache: Redis（后续）
Object Storage: MinIO（后续）
Docker: 暂时不用
Production Target: Ubuntu 24.04 + Docker Compose
```

## 当前阶段

当前不是业务开发阶段。

当前是：

```text
First Runnable Skeleton
```

目标是让项目第一次在 Windows 本地启动。

## 当前任务

```text
TASK-002W
```

## 关键约束

虽然在 Windows 下运行，但代码必须 Linux / Docker Ready。

禁止：

```text
D:\path\to\file
C:\xxx
win32api
Windows 专属服务
硬编码路径
真实密钥
```

必须：

```text
pathlib.Path
.env
.env.example
相对路径
跨平台命令
```

## 国内软件源

必须优先使用中国境内镜像源：

- Python pip：清华源优先
- Node npm：npmmirror 优先
- 未来 Docker：配置国内镜像加速，保留官方源切换能力
