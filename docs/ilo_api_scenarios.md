# HPE iLO RESTful API (Redfish) 测试指南

本指南详细说明了 HPE ProLiant 服务器 iLO RESTful API 的测试路径、场景以及官方容器的使用建议。

## 1. 官方 Docker 容器说明 (Official Container Status)

**问：这是官方那边的 Docker 容器吗？**

**答：** HPE 官方维护了 **iLO Redfish Interface Emulator** 的源代码，但并没有在 Docker Hub 上提供一个名为 "official" 的预构建镜像。

*   **官方仓库**: [HewlettPackard/ilo-redfish-emulator](https://github.com/HewlettPackard/ilo-redfish-emulator)
*   **建议**: 如果您需要一个高度兼容的模拟器，建议克隆上述仓库并自行构建。
*   **自行构建命令**:
    ```bash
    git clone https://github.com/HewlettPackard/ilo-redfish-emulator.git
    cd ilo-redfish-emulator
    docker build -t ilo-redfish-emulator .
    docker run -p 5000:5000 ilo-redfish-emulator
    ```

---

## 2. iLO Redfish API 测试路径与场景 (Test Paths & Scenarios)

除了常见的 `/redfish/v1/Systems/1` 之外，以下是针对 HPE iLO 优化的测试路径和场景。

### A. 系统清单与状态 (System Inventory & Health)
| Redfish Path | English Scenario | 中文测试场景 |
| :--- | :--- | :--- |
| `/redfish/v1/Systems/1/Processors` | Verify CPU count, model, and health status. | 验证 CPU 的数量、型号及健康状态。 |
| `/redfish/v1/Systems/1/Memory` | Check memory capacity and DIMM slot status. | 检查内存总容量及各插槽内存条状态。 |
| `/redfish/v1/Systems/1/NetworkInterfaces` | Retrieve NIC adapter details and MAC addresses. | 获取网卡适配器详情及 MAC 地址。 |

### B. 电源与温度 (Power & Thermal)
| Redfish Path | English Scenario | 中文测试场景 |
| :--- | :--- | :--- |
| `/redfish/v1/Chassis/1/Power` | Monitor real-time power consumption and PSU health. | 监控实时功耗、电源模块状态及冗余性。 |
| `/redfish/v1/Chassis/1/Thermal` | Verify fan speeds and ambient temperature sensors. | 验证风扇转速是否正常，监控各位置温度。 |
| `POST .../Actions/ComputerSystem.Reset` | Power cycle: Execute GracefulRestart or ForceOff. | 电源控制：执行正常重启、强制关机或开机操作。 |

### C. 存储管理 (Storage Management)
| Redfish Path | English Scenario | 中文测试场景 |
| :--- | :--- | :--- |
| `/redfish/v1/Systems/1/Storage` | List RAID controllers (e.g., Smart Array). | 列出服务器内的存储控制器（如 Smart Array）。 |
| `/redfish/v1/Systems/1/Storage/1/Drives` | Monitor health of individual physical drives. | 监控每一块物理硬盘的健康状况。 |
| `/redfish/v1/Systems/1/Storage/1/Volumes` | Verify logical drive (RAID volume) configurations. | 验证逻辑卷（RAID 阵列）的配置和状态。 |

### D. 日志与维护 (Logs & Maintenance)
| Redfish Path | English Scenario | 中文测试场景 |
| :--- | :--- | :--- |
| `/redfish/v1/Managers/1/LogServices/IML/Entries` | Read Integrated Management Log (IML) events. | 读取集成管理日志（IML），用于硬件故障回溯。 |
| `/redfish/v1/Managers/1/LogServices/IEL/Entries` | Read iLO Event Log (IEL) for management events. | 读取 iLO 事件日志，监控管理芯片的行为。 |
| `/redfish/v1/UpdateService/FirmwareInventory` | Check firmware versions for iLO, BIOS, and NICs. | 检查 iLO、BIOS、网卡等组件的固件版本。 |

### E. iLO 管理配置 (iLO Manager Config)
| Redfish Path | English Scenario | 中文测试场景 |
| :--- | :--- | :--- |
| `/redfish/v1/Managers/1/EthernetInterfaces/1` | Get/Set iLO static IP or DHCP configuration. | 获取或设置 iLO 管理网口的静态 IP 或 DHCP 配置。 |
| `/redfish/v1/AccountService/Accounts` | Manage iLO local user accounts and privileges. | 管理 iLO 本地用户账户及其权限级别。 |

---

## 3. 示例：使用 cURL 进行快速测试 (Quick Test Examples)

```bash
# 获取系统摘要
curl -u admin:password -k https://<iLO_IP>/redfish/v1/Systems/1

# 获取电源状态
curl -u admin:password -k https://<iLO_IP>/redfish/v1/Chassis/1/Power

# 执行服务器冷重启 (ForceRestart)
curl -u admin:password -k -X POST \
  -H "Content-Type: application/json" \
  -d '{"ResetType": "ForceRestart"}' \
  https://<iLO_IP>/redfish/v1/Systems/1/Actions/ComputerSystem.Reset
```

> [!TIP]
> 在生产环境中，建议使用 `https` 端口（通常为 443）并带上用户凭据。对于模拟器环境，通常使用 `http` 和 5000 端口。
