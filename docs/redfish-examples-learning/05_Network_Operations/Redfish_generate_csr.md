# Redfish_generate_csr

## Definition / 定义
**EN**: This script triggers iLO to generate a Certificate Signing Request (CSR) which can then be sent to a Certificate Authority (CA).
**ZH**: 此脚本触发 iLO 生成证书签名请求 (CSR)，然后可以将其发送到证书颁发机构 (CA)。

## Use Case / 使用场景
**EN**: Automating the SSL certificate renewal process for iLO management interfaces to replace untrusted self-signed certificates.
**ZH**: 自动化 iLO 管理接口的 SSL 证书更新过程，以替换不可信的自签名证书。

## Reference / 参考
- **Example Name**: `Redfish_generate_csr`
- **Source Code**: [generate_csr.py](https://github.com/HewlettPackard/python-ilorest-library/blob/master/examples/Redfish/generate_csr.py)
