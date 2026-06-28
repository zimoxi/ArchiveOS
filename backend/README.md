# Backend

后端代码目录。Hermes 在收到任务前不得自行创建复杂业务代码。

## 环境要求

- Python 3.11+

## 国内软件源配置

```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

## 安装依赖

```bash
cd backend
python -m venv .venv
.venv\\Scripts\\activate      # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## 启动

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 验证

```bash
curl http://127.0.0.1:8000/health
# {"status":"ok","service":"openfdams-backend"}
```

