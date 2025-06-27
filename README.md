# 🔐 Bitcoin Brute Force Address Scanner

> 🚨 **免责声明：本项目仅用于学习密码学与区块链技术，请勿用于任何非法行为。使用者需自行承担一切法律责任。**

一个基于 Python 的比特币撞币演示程序：自动生成私钥 → 推导地址 → 查询链上余额 → 命中则保存结果。

---

## 📦 安装依赖

```bash
pip install ecdsa base58 requests
```

---

## 🚀 使用方法

运行程序：

```bash
python main.py
```

程序会不断生成地址并查询余额，命中后会保存至 `found.txt`。

---

## 🔗 示例输出

```text
检查地址: 1CXY2uJW6iyg12LwCFAshyd9X3qDj5DRvm
地址余额（satoshi）: 0
检查地址: 1KsTXYZW6gHT8E2XcD9Sx4gVi1WT88oSyU
🎯 找到余额地址！
地址: 1KsTXYZW6gHT8E2XcD9Sx4gVi1WT88oSyU
私钥(hex): fbd1a6c2b3e3b...
```

---

## 🔍 默认余额查询接口

默认使用 blockchain.info 的余额接口：

```text
https://blockchain.info/balance?active={address}
```

---

## 📄 License

MIT License
