import network
import time

# Wi-Fi 設定
SSID = 'DoraHome300M'  # 替換為你的 Wi-Fi 名稱
PASSWORD = '0975393503@'  # 替換為你的 Wi-Fi 密碼

# 創建 STA（Station）接口
wlan = network.WLAN(network.STA_IF)

# 啟用 STA 模式
wlan.active(True)

# 連接 Wi-Fi 網路
wlan.connect(SSID, PASSWORD)

# 等待連接完成
print('連接中...')
while not wlan.isconnected():
    time.sleep(1)
    print('嘗試連接...')

# 顯示連接結果
if wlan.isconnected():
    print('已連接')
    print('網路設定:', wlan.ifconfig())
else:
    print('連接失敗')
