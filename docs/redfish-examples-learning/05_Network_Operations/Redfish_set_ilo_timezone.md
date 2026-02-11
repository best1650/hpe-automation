# Redfish_set_ilo_timezone

## Definition / 定义
**EN**: This script sets the local time zone on the iLO manager, ensuring that log entries reflect the correct local time.
**ZH**: 此脚本在 iLO 管理器上设置本地时区，确保日志条目反映正确的本地时间。

## Use Case / 使用场景
**EN**: Global server deployment where each hardware unit must be configured with its local data center's time zone for accurate incident reporting.
**ZH**: 全球服务器部署，每个硬件单元必须配置其本地数据中心的时区，以便准确报告事件。

## Reference / 参考
- **Example Name**: `Redfish_set_ilo_timezone`
- **Source Code**: [set_ilo_timezone.py](https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/set_ilo_timezone.py)
