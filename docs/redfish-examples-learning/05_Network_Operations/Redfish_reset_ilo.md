# Redfish_reset_ilo

## Definition / 定义
**EN**: This script triggers a reset of the iLO management processor itself, which can resolve persistent management connectivity issues.
**ZH**: 此脚本触发 iLO 管理处理器本身的重置，这可以解决持久的管理连接问题。

## Use Case / 使用场景
**EN**: Refreshing the iLO management interface when the web UI or API becomes sluggish or unresponsive, without affecting the running host OS.
**ZH**: 当 Web 用户界面或 API 变得缓慢或无响应时，刷新 iLO 管理接口，而不影响运行中的宿主操作系统。

## Reference / 参考
- **Example Name**: `Redfish_reset_ilo`
- **Source Code**: [reset_ilo.py](https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/reset_ilo.py)
