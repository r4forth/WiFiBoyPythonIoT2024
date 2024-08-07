# 05_01. 讓你的玩學機點亮機器內建的 LED，並間隔 1 秒持續閃爍。
from machine import Pin
from time import sleep

# 定義 LED 的輸出腳位，WiFiBoy Python IoT 是 Pin 16
led = Pin(16, Pin.OUT)

print('請把機器翻背面: 觀看內建 LED 的狀態: ')
while True:
    led.value(1)  # 關閉 LED
    sleep(1)      # 延遲 1 秒
    print('滅')
    led.value(0)  # 開啟 LED
    sleep(1)      # 延遲 1 秒
    print('亮')