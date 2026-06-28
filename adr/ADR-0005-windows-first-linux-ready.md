# ADR-0005 Windows First, Linux Ready

## Status

Accepted

## 背景

用户当前在 Windows 环境开发，暂时不能使用 Docker。  
但 OpenFDAMS 未来需要部署到 Linux + Docker 环境。

## 决策

采用：

```text
Windows First, Linux Ready
```

即：

- 开发阶段优先支持 Windows 原生运行
- 生产部署目标仍为 Linux + Docker
- 代码必须跨平台
- 不允许写 Windows 专属逻辑

## 后果

优点：

- 用户可以立即开始本地试运行
- 不依赖 Docker
- 降低早期开发阻力

代价：

- 需要严格控制路径、环境变量和依赖管理
- 后续必须补充 Docker 验证
