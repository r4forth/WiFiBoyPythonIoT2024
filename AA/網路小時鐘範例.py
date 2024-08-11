# 13.03 網路時鐘
from machine import Pin, SoftI2C
import network, ntptime, time

# WiFi 設定
SSID = 'DoraHome300M'     # 更換成你家的 WiFi SSID
PASSWORD = '0975393503@'  # 更換成你家的 WiFi 密碼

# 連接 WiFi 程式
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print("WiFi connected:", wlan.ifconfig())
# 取得網路時間
def get_network_time():
    retry_count = 5
    for _ in range(retry_count):
        try:
            ntptime.settime()
            tm = time.localtime()
            return tm[3], tm[4], tm[5]  # 返回小時、分鐘與秒數
        except OSError as e:
            print("Failed to get time, retrying...")
            time.sleep(2)  # 等待2秒後重試
    raise Exception("Failed to get network time after several attempts.")



i2c = SoftI2C(scl = Pin(22), sda = Pin(23))
# 顯示數值函數
def displayNum(num, colon_on):
    d = bytearray(1)
    brightness = 1
    d[0] = brightness * 16 + 1          # xbbbbxxxd b = brightness d = on/off
    i2c.writeto(0x24, d)                # 打開
    digits = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]
    numbers= [   0,    1,    2,    3,    4,    5,    6,    7,    8,    9]
    
    if num < 0:
        num = 0
    elif num > 9999:
        num = 9999
    number_to_display = [num // 1000 % 10, num // 100 % 10, num // 10 % 10, num % 10]
    digit_to_display = [digits[number_to_display[0]], digits[number_to_display[1]], digits[number_to_display[2]], digits[number_to_display[3]]]
    # 在第二位數字後加入冒號（用於閃爍）
    if colon_on:
        digit_to_display[1] |= 0x80  # 0x80 用於顯示冒號
    
    digit = bytes(digit_to_display)
    for i in range(4):
        d[0] = digit[i]
        i2c.writeto(0x34+i, d)          # 顯示四位數字
# 取得時間函數
def getTime():
    hour, minute, second = get_network_time()
    time_to_display = (hour + 8) * 100 + minute
    colon_on = (second % 2 == 0)  # 每秒閃爍冒號
    displayNum(time_to_display, colon_on)

# 主程式
connect_wifi()
while True:
    getTime()
    time.sleep(1)  # 每秒鐘更新一次