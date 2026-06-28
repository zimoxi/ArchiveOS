# MIRROR_STANDARD

## 目标

所有依赖下载优先使用中国境内软件源，以提升开发速度和稳定性。

## Python

默认：

```text
清华大学 PyPI 源
```

命令：

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## Node.js

默认：

```text
npmmirror
```

命令：

```bash
npm config set registry https://registry.npmmirror.com
```

## Docker

当前不用 Docker。

未来 Docker 阶段应支持：

- 国内镜像加速
- 官方源回退
- 不在 Dockerfile 中硬编码不可切换源

## 原则

镜像源配置必须可切换，不得把某个供应商写死在业务代码中。
