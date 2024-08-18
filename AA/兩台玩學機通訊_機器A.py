# 兩台 WiFiBoy 連線通訊
# UART 通訊
# 我是機器A
# IO5   ---> TX
# IO21  ---> RX
from machine import UART, Pin
import time

# 設定 UART 1，鮑率為 9600
uart1 = UART(1, baudrate=9600, tx=Pin(5), rx=Pin(21))
led = Pin(16, Pin.OUT)
led.value(0)
print('Machine A Ready!')

# 發送清除螢幕的訊息給機器B
uart1.write("CLEAR_SCREEN")

# 等待機器B回應
while True:
    if uart1.any():
        response = uart1.read().decode('utf-8')
        if response == "Clear Screen Done!":
            wb.cls()
            wb.str("Machine B Screen Cleaned", 10, 10, 2)  # 在螢幕上顯示訊息
            print("Received from Machine B:", response)
            break

time.sleep(1)