# WINDOWS_DEVELOPMENT_STANDARD

## Windows 开发目标

让用户可以在 Windows 本地直接启动 OpenFDAMS。

## 推荐工具

- Python 3.12
- Node.js LTS
- Git
- VS Code
- PowerShell
- PostgreSQL Windows版（后续）
- Redis Windows兼容版本或 Memurai（后续）
- MinIO Windows EXE（后续）

## 必须提供脚本

```text
scripts/start_backend.bat
scripts/start_frontend.bat
scripts/start_all.bat
```

## 脚本要求

- 不写死用户目录
- 使用项目相对路径
- 能在项目根目录执行
- 出错时暂停窗口，方便查看错误
