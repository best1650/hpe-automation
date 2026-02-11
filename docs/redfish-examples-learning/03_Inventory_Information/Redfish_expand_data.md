# Redfish_expand_data

## Definition / 定义
**EN**: This script demonstrates how to use the `$expand` query parameter to retrieve nested data structures in a single API call, reducing the number of requests.
**ZH**: 此脚本演示了如何使用 `$expand` 查询参数在单个 API 调用中获取嵌套的数据结构，从而减少请求次数。

## Use Case / 使用场景
**EN**: Optimizing dashboard performance by fetching all chassis and system details in one go instead of looping through individual resource URIs.
**ZH**: 通过一次性获取所有机箱和系统详情，而不是循环访问单个资源 URI，来优化仪表板性能。

## Reference / 参考
- **Example Name**: `Redfish_expand_data`
- **Source Code**: [expand_data.py](https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/expand_data.py)
