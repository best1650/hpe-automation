# Redfish_find_ilo_mac_address

## Definition / 定义
**EN**: This script specifically extracts the MAC address of the iLO management processor, which is useful for network provisioning and switch configuration.
**ZH**: 此脚本专门提取 iLO 管理处理器的 MAC 地址，这对于网络配置和交换机配置非常有用。

## Use Case / 使用场景
**EN**: Generating a list of MAC addresses for DHCP reservation and VLAN assignment prior to deploying hundreds of servers.
**ZH**: 在部署数百台服务器之前，生成用于 DHCP 保留和 VLAN 分配的 MAC 地址列表。

## Reference / 参考
- **Example Name**: `Redfish_find_ilo_mac_address`
- **Source Code**: [find_ilo_mac_address.py](https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/find_ilo_mac_address.py)
