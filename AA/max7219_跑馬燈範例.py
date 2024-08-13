# Max7219 範例_HelloWorld跑馬燈
from machine import Pin, SPI
import lib.max7219
from utime import sleep

CLOCK_PIN = 18
DATA_PIN = 23
CS_PIN = 5

spi0 = SPI(2, baudrate=10000000, polarity=0, phase=0, sck=Pin(CLOCK_PIN), mosi=Pin(DATA_PIN))
cs = Pin(CS_PIN, Pin.OUT)

matrix = lib.max7219.Matrix8x8(spi0, cs, 4)

# 顯示字串函數
def clear_display():
    # 清除顯示內容
    matrix.fill(0)
    matrix.show()

def show_text(text, delay=0.1):
    text_width = len(text) * 8
    clear_display()
    for offset in range(text_width + 32):  # 32 是為了讓文字全部移出螢幕
        clear_display()
        for i in range(len(text)):
            char = text[i]
            # 計算字在螢幕上的起始位置
            char_x = (i * 8) - offset
            if -8 < char_x < 128:  # 只顯示螢幕內的字串
                matrix.text(char, char_x, 0, 1)
        matrix.show()
        sleep(delay)

# 執行跑馬燈程式
try:
    while True:
        show_text("Hello, WiFiBoy!")
except KeyboardInterrupt:
    clear_display()
