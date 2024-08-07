# 05_03. 當按下 A 鍵，清除螢幕畫面並將背景設定為粉紅色，機器後面的 LED 開始閃爍
from machine import Pin
from time import sleep

# 定義 LED 的輸出腳位，WiFiBoy Python IoT Pin 27 控制玩學機的背光 
led1 = Pin(16, Pin.OUT)
led2 = Pin(27, Pin.OUT)
LEDState = 0
print('請觀察: 觀看正面 LCD 面板與背面 LED 的狀態: ')

wb.cls(wb.BLUE)
while True:
    if wb.getkey() == 2:
        led1.value(LEDState)
        led2.value(LEDState)
        LEDState = not LEDState
    time.sleep(1)