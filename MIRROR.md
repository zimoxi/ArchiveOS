# MIRROR

## Python pip

默认使用清华大学源：

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

备用：

```text
https://mirrors.ustc.edu.cn/pypi/simple/
https://mirrors.aliyun.com/pypi/simple/
```

## Node npm

默认使用 npmmirror：

```bash
npm config set registry https://registry.npmmirror.com
```

## pnpm

```bash
pnpm config set registry https://registry.npmmirror.com
```

## Docker

当前 Windows 开发阶段不使用 Docker。

未来 Linux / Docker 阶段必须支持国内镜像加速，但 Dockerfile 不得写死单一镜像源。

## Git

主仓库仍使用 GitHub。  
如国内访问不稳定，可增加 Gitee 镜像，但 GitHub 仍作为主仓库。
