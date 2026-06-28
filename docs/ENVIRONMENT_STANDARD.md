# ENVIRONMENT_STANDARD

## 开发策略

OpenFDAMS 采用：

```text
Windows First, Linux Ready
```

即：

- Windows 用于日常开发和试运行
- Linux + Docker 用于未来部署
- 代码只有一份
- 环境通过配置区分

## 跨平台要求

必须使用：

```python
from pathlib import Path
```

禁止：

```text
硬编码 C:\ 或 D:\
Windows API
平台专属服务
```

## 配置要求

所有可变配置必须写入：

```text
.env
.env.example
```

`.env` 不进入 Git。

## 启动方式

Windows 使用 `.bat` 脚本。  
Linux / Docker 后续使用 Docker Compose。  
两者必须调用同一套 Python / Node 代码。
