import os
import time
import base58
import hashlib
import requests
from ecdsa import SigningKey, SECP256k1

# 生成私钥
def generate_private_key():
    return os.urandom(32)

# 获取公钥（压缩格式）
def private_key_to_public_key(private_key_bytes):
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    vk = sk.verifying_key
    x = vk.pubkey.point.x()
    y = vk.pubkey.point.y()
    return (b'\x02' if y % 2 == 0 else b'\x03') + x.to_bytes(32, 'big')

# 获取 BTC/BTN 地址（P2PKH，Base58Check）
def public_key_to_address(public_key):
    sha256_pub = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160', sha256_pub).digest()
    prefixed = b'\x00' + ripemd160  # Mainnet prefix 0x00
    checksum = hashlib.sha256(hashlib.sha256(prefixed).digest()).digest()[:4]
    return base58.b58encode(prefixed + checksum).decode()

# 查询地址余额（这里用 BTN 区块浏览器接口，示例为 btnexplorer.com）
def check_btn_balance(address):
    try:
        url = f"https://blockchain.info/balance?active={address}"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            balance_satoshi = data[address]["final_balance"]
            print(f"地址余额（satoshi）: {balance_satoshi}")
            return balance_satoshi > 0
    except Exception as e:
        print(f"查询失败: {e}")
    return False

# 主程序
while True:
    priv = generate_private_key()
    pub = private_key_to_public_key(priv)
    addr = public_key_to_address(pub)

    print(f"检查地址: {addr}")
    if check_btn_balance(addr):
        print("🎯 找到余额地址！")
        print(f"地址: {addr}")
        print(f"私钥(hex): {priv.hex()}")
        with open("found.txt", "a") as f:
            f.write(f"{addr} - {priv.hex()}\n")
        break
    time.sleep(1)  # 可移除或调小，提高速度
