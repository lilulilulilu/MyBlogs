# MCP Server Kubernetes 部署指南

这是一个基于 FastMCP 框架的 MCP (Model Context Protocol) 服务器，支持通过 Helm 部署到 Kubernetes 集群。

## 项目结构

```
mcp/
├── server.py              # MCP 服务器主文件
├── requirements.txt       # Python 依赖
├── Dockerfile            # Docker 镜像构建文件
├── deploy.sh             # 简单 Docker 部署脚本
├── helm/                 # Helm Chart 目录
│   └── mcp-server/
│       ├── Chart.yaml    # Helm Chart 元数据
│       ├── values.yaml   # 默认配置值
│       └── templates/    # Kubernetes 资源模板
│           ├── _helpers.tpl
│           ├── deployment.yaml
│           ├── service.yaml
│           └── serviceaccount.yaml
└── README.md             # 本文档
```

## 功能特性

### 工具函数 (Tools)
- `add(a: int, b: int) -> int`: 加法运算
- `sub(a: int, b: int) -> int`: 减法运算
- `mul(a: int, b: int) -> int`: 乘法运算
- `get_weather(city: str) -> str`: 获取城市天气信息

### 资源函数 (Resources)
- `greeting://{name}`: 获取个性化问候语
- `file://documents/{name}`: 读取文档内容

### 提示函数 (Prompts)
- `review_code(code: str) -> str`: 代码审查提示模板

## 部署步骤

### 前置要求

- Docker Desktop 或 Docker Engine
- Kubernetes 集群 (推荐 Docker Desktop Kubernetes)
- kubectl 命令行工具
- Helm 3.x

### 1. 构建 Docker 镜像

```bash
# 进入项目目录
cd /Users/lu/Documents/codes/MyBlogs/AI/chatbot/mcp

# 构建 Docker 镜像
docker build -t mcp-server:latest .
```

### 2. 验证镜像构建

```bash
# 查看构建的镜像
docker images | grep mcp-server

# 可选：本地测试运行
docker run -d -p 8002:8002 mcp-server:latest
```

### 3. 使用 Helm 部署到 Kubernetes

```bash
# 部署到 Kubernetes
helm install mcp-server ./helm/mcp-server

# 查看部署状态
helm status mcp-server
```

### 4. 验证部署

```bash
# 检查 Pod 状态
kubectl get pods -l app.kubernetes.io/name=mcp-server

# 检查 Service 状态
kubectl get services -l app.kubernetes.io/name=mcp-server

# 查看 Pod 日志
kubectl logs -l app.kubernetes.io/name=mcp-server
```

### 5. 访问服务

服务通过 NodePort 暴露，可以通过以下方式访问：

```bash
# 本地访问
curl http://localhost:30080

# 或使用 kubectl port-forward
kubectl port-forward service/mcp-server 8002:8002
```

## 配置说明

### Helm Values 配置

主要配置项在 `helm/mcp-server/values.yaml` 中：

```yaml
# 镜像配置
image:
  repository: mcp-server
  pullPolicy: Never  # 使用本地镜像
  tag: "latest"

# 服务配置
service:
  type: NodePort
  port: 8002
  nodePort: 30080

# 资源限制
resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 100m
    memory: 128Mi

# MCP 服务器配置
mcp:
  serverName: "Demo"
  serverPort: 8002
  serverHost: "0.0.0.0"
  transport: "streamable-http"
```

### 环境变量

服务器使用以下环境变量：

- `SERVER_NAME`: 服务器名称 (默认: "Demo")
- `SERVER_PORT`: 服务器端口 (默认: 8002)
- `SERVER_HOST`: 服务器主机 (默认: "0.0.0.0")
- `TRANSPORT`: 传输协议 (默认: "streamable-http")

## 管理命令

### 升级部署

```bash
# 修改配置后升级
helm upgrade mcp-server ./helm/mcp-server

# 查看升级历史
helm history mcp-server
```

### 回滚部署

```bash
# 回滚到上一个版本
helm rollback mcp-server

# 回滚到指定版本
helm rollback mcp-server 1
```

### 卸载部署

```bash
# 卸载 Helm Release
helm uninstall mcp-server

# 清理资源
kubectl delete pvc --all
```

## 故障排除

### 常见问题

1. **Pod 启动失败**
   ```bash
   # 查看 Pod 详细信息
   kubectl describe pod -l app.kubernetes.io/name=mcp-server
   
   # 查看 Pod 日志
   kubectl logs -l app.kubernetes.io/name=mcp-server
   ```

2. **镜像拉取失败**
   - 确保使用 `imagePullPolicy: Never`
   - 检查本地镜像是否存在：`docker images | grep mcp-server`

3. **服务无法访问**
   ```bash
   # 检查 Service 配置
   kubectl get service mcp-server -o yaml
   
   # 检查端口映射
   kubectl get endpoints mcp-server
   ```

4. **健康检查失败**
   - MCP 服务器默认没有 HTTP 健康检查端点
   - 已在配置中禁用健康检查

### 调试命令

```bash
# 进入 Pod 调试
kubectl exec -it <pod-name> -- /bin/bash

# 查看所有资源
kubectl get all -l app.kubernetes.io/name=mcp-server

# 查看 Helm Release 详细信息
helm get all mcp-server
```

## 开发说明

### 本地开发

```bash
# 安装依赖
pip install -r requirements.txt

# 运行服务器
python server.py
```

### 添加新功能

1. 在 `server.py` 中添加新的工具、资源或提示函数
2. 重新构建 Docker 镜像
3. 升级 Helm 部署

### 自定义配置

修改 `helm/mcp-server/values.yaml` 中的配置，然后运行：

```bash
helm upgrade mcp-server ./helm/mcp-server
```

## 测试
```shell
python client.py
```

## 技术栈

- **Python 3.11**: 运行环境
- **FastMCP**: MCP 服务器框架
- **Docker**: 容器化
- **Kubernetes**: 容器编排
- **Helm**: 包管理
- **Uvicorn**: ASGI 服务器

## 许可证

本项目遵循 MIT 许可证。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。
