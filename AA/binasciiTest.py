# 07_01.binasciiTest.py
import binascii

# 範例二進制數據
binary_data = b'Hello, WiFiBoy!'

# 二進制數據轉十六進制表示
hex_string = binascii.hexlify(binary_data)
print("十六進制表示:", hex_string)

# 十六進制表示轉回二進制數據
decoded_data = binascii.unhexlify(hex_string)
print("解碼後的二進制數據:", decoded_data)

# 二進制數據編碼為 Base64 表示
base64_string = binascii.b2a_base64(binary_data).strip()  # .strip() 去掉末尾的換行符
print("Base64 表示:", base64_string)

# Base64 表示解碼回二進制數據
decoded_base64_data = binascii.a2b_base64(base64_string)
print("解碼後的 Base64 二進制數據:", decoded_base64_data)