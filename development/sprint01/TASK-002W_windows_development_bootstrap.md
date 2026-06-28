# TASK-002W Windows 本地开发环境初始化

## 目标

让 OpenFDAMS 在 Windows 本地具备第一个可运行工程骨架的准备条件。

本任务不要求实现业务功能，只建立工程结构、依赖文件和启动脚本。

## 必须新增 / 更新

```text
backend/
  app/
    main.py
  requirements.txt
  README.md

frontend/
  package.json
  index.html
  src/
    main.ts
    App.vue
  vite.config.ts
  README.md

scripts/
  start_backend.bat
  start_frontend.bat
  start_all.bat

.env.example
```

## Backend 要求

- 使用 FastAPI
- 提供 `/health`
- 返回：

```json
{"status":"ok","service":"openfdams-backend"}
```

- 使用 Python 3.12
- requirements.txt 优先包含：

```text
fastapi
uvicorn[standard]
pydantic
pydantic-settings
python-dotenv
```

## Frontend 要求

- 使用 Vue 3 + Vite + TypeScript
- 首页显示：

```text
OpenFDAMS / ArchiveOS
Windows Development Mode
```

## 国内软件源

必须在 README 中写明：

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
npm config set registry https://registry.npmmirror.com
```

## Windows 启动脚本

### start_backend.bat

应进入 backend，创建/使用虚拟环境，安装依赖，启动 FastAPI。

### start_frontend.bat

应进入 frontend，安装依赖，启动 Vite。

### start_all.bat

打开两个窗口分别启动 backend 和 frontend。

## 禁止

- 不做数据库
- 不做登录
- 不做档案业务
- 不做权限系统
- 不做 Docker
- 不写 Windows 绝对路径

## 验收

- `scripts/start_backend.bat` 可启动后端
- `http://127.0.0.1:8000/health` 可访问
- `scripts/start_frontend.bat` 可启动前端
- `http://localhost:5173` 可访问
- Git 工作树干净
