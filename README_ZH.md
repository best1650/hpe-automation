# HPE iLO 模拟器 - 使用说明文档

本指南介绍了如何在 Mac M3 Pro 上运行并使用 HPE iLO 模拟器（包含 API 和 Web UI）。

## 1. 环境准备
- **Docker Desktop**: 确保 Docker Desktop 已启动。
- **Python 3.9+**: 用于运行本地自动化测试（可选）。

## 2. 启动模拟器
模拟器已容器化。使用 Docker Compose 进行构建和启动：

```bash
# 构建并以分离模式启动容器
docker compose up -d --build
```

等待几秒钟，确保 Flask 服务器初始化完成。

## 3. 访问 Web UI
模拟器提供了一个现代化的 iLO 风格 Web 界面。

- **访问地址**: [http://localhost:5000](http://localhost:5000)
- **登录凭据**:
  - **用户名**: `admin`
  - **密码**: `password`

登录成功后，您将被重定向到 **Information Overview**（信息概览）仪表盘，查看系统健康状况和详细信息。

## 4. 使用 Redfish API
模拟器实现了 DMTF Redfish 标准。您可以使用 `curl` 或任何 API 客户端查询系统信息。

### 获取系统详细信息
```bash
curl http://localhost:5000/redfish/v1/Systems/1
```

### 预期响应片段
```json
{
    "Manufacturer": "HPE",
    "Model": "ProLiant DL380 Gen10",
    "PowerState": "On",
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    }
}
```

## 5. 运行自动化测试
如果您已经配置了 `.venv`，可以运行 Robot Framework 测试：

```bash
# API 测试
source .venv/bin/activate
robot tests/redfish_api.robot

# UI 测试（需要安装 Chrome）
robot tests/ilo_ui.robot
```

## 6. 停止模拟器和 Web UI
要停止模拟器并关闭 Web UI/API，请根据您的启动方式选择以下方法之一：

### 方法 A: 使用 Docker Compose (推荐)
```bash
docker compose down
```

### 方法 B: 使用 Docker 直接命令
如果您是使用 `docker run` 启动的容器，请运行：
```bash
# 停止并删除容器
docker stop ilo-simulator && docker rm ilo-simulator
```

容器停止后，[http://localhost:5000](http://localhost:5000) 上的 Web UI 将无法再访问。
