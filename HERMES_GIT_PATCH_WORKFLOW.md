# Hermes Git Patch 工作规范

你正在维护同一个项目：ArchiveOS / OpenFDAMS。

不要新建项目。不要覆盖项目。不要删除已有代码。不要重构无关模块。

## 收到 Delivery 包后的流程

1. 执行 `git status`
2. 解压 Delivery 到临时目录，不要直接覆盖项目
3. 阅读 README_UPDATE.md、PATCH.md、MERGE_GUIDE.md、CURRENT_STATUS.md、NEXT_ACTION.md
4. 按 MERGE_GUIDE 合并文件
5. 只执行 NEXT_ACTION.md 指定任务
6. 运行检查
7. `git add . && git commit -m "apply DeliveryXXX patch"`
8. 输出执行报告
