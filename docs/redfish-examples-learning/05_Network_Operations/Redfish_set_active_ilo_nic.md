# Redfish_set_active_ilo_nic

## Definition / 定义
**EN**: This script allows you to toggle which physical NIC port is active for iLO management (e.g., dedicated port vs shared LOM).
**ZH**: 此脚本允许您切换哪个物理网卡端口用于 iLO 管理（例如，专用端口与共享 LOM）。

## Use Case / 使用场景
**EN**: Switching management traffic to a secondary network bond or dedicated management network during a data center infrastructure upgrade.
**ZH**: 在数据中心基础设施升级期间，将管理流量切换到辅助网络绑定或专用管理网络。

## Reference / 参考
- **Example Name**: `Redfish_set_active_ilo_nic`
- **Source Code**: [set_active_ilo_nic.py](https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/set_active_ilo_nic.py)
