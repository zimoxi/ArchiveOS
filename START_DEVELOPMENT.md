# START_DEVELOPMENT

## 这是 Hermes 的唯一开发入口

Hermes 启动后只需要阅读本文件，不要扫描整个仓库。

## 当前任务

```text
TASK-002W：Windows 本地开发环境初始化
```

## 必须按顺序阅读

1. `PROJECT_STATE.json`
2. `CURRENT_CONTEXT.md`
3. `TASK_QUEUE.md`
4. `NEXT_ACTION.md`
5. `development/sprint01/TASK-002W_windows_development_bootstrap.md`
6. `docs/ENVIRONMENT_STANDARD.md`
7. `docs/MIRROR_STANDARD.md`
8. `docs/WINDOWS_DEVELOPMENT_STANDARD.md`
9. `docs/LINUX_DOCKER_COMPATIBILITY_STANDARD.md`

## 不需要阅读

本任务不需要阅读：

- blueprint/
- specs/
- epics/
- ai/
- migration/
- future sprint files

## 当前目标

让 OpenFDAMS 在 Windows 本地第一次具备“可运行工程骨架”。

## 当前不做

- 不开发 Archive
- 不开发 Borrow
- 不开发 Permission
- 不开发 AI
- 不开发 OCR
- 不接数据库业务表
- 不使用 Docker

## 完成后

执行：

```bash
git status
git add .
git commit -m "feat: initialize Windows runnable development skeleton"
git push origin main
```

然后输出执行报告。
