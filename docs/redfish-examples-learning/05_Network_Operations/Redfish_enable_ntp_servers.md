# Redfish_enable_ntp_servers

## Definition / 定义
**EN**: This script enables Network Time Protocol (NTP) on the iLO and allows you to specify the primary and secondary time servers.
**ZH**: 此脚本在 iLO 上启用网络时间协议 (NTP)，并允许您指定主备网络时间服务器。

## Use Case / 使用场景
**EN**: Ensuring all server logs across the network have synchronized timestamps, which is critical for security audit log analysis.
**ZH**: 确保网络中所有服务器日志的时间戳同步，这对于安全审计日志分析至关重要。

## Reference / 参考
- **Example Name**: `Redfish_enable_ntp_servers`
- **Source Code**: [enable_ntp_servers.py](https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/enable_ntp_servers.py)
