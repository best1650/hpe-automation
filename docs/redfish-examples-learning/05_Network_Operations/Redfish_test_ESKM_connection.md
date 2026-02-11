# Redfish_test_ESKM_connection

## Definition / 定义
**EN**: This script performs a connectivity test between the iLO and the configured ESKM server to verify that encryption key requests will be successful.
**ZH**: 此脚本执行 iLO 与配置的 ESKM 服务器之间的连接测试，以验证加密密钥请求是否会成功。

## Use Case / 使用场景
**EN**: Periodic health checks of the encryption infrastructure to alert administrators if the key management server becomes unreachable.
**ZH**: 定期对加密基础设施进行健康检查，以便在密钥管理服务器无法访问时提醒管理员。

## Reference / 参考
- **Example Name**: `Redfish_test_ESKM_connection`
- **Source Code**: [test_ESKM_connection.py](https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/test_ESKM_connection.py)
