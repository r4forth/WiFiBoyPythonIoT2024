# 05_02. 操作 LCD 背光，並將 LCD 畫面設定為藍色。
from machine import Pin
from time import sleep

# 定義 LED 的輸出腳位，WiFiBoy Python IoT Pin 27 控制玩學機的背光 
led = Pin(27, Pin.OUT)

print('請觀察: 觀看正面 LCD 面板的狀態: ')
wb.cls(wb.BLUE)
while True:
    led.value(1)    # 開啟 LCD 背光
    sleep(0.6)      # 延遲 0.6 秒
    print('LCD 背光亮')
    led.value(0)    # 關閉 LED 背光
    sleep(0.4)      # 延遲 0.4 秒
    print('LCD 背光滅')