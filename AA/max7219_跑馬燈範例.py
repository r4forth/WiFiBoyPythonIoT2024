# Max7219範例_HelloWorld跑馬燈
from machine import Pin, SPI
import lib.max7219
from utime import sleep

# 定义引脚
CLOCK_PIN = 18
DATA_PIN = 23
CS_PIN = 5

# 初始化 SPI
spi0 = SPI(2, baudrate=10000000, polarity=0, phase=0, sck=Pin(CLOCK_PIN), mosi=Pin(DATA_PIN))

# 初始化 Chip Select 引脚
cs = Pin(CS_PIN, Pin.OUT)

# 初始化 MAX7219 LED 矩阵
matrix = lib.max7219.Matrix8x8(spi0, cs, 4)

# 显示字符的函数
def clear_display():
    # 清除显示：将所有字节设置为 0
    matrix.fill(0)
    matrix.show()

def show_text(text, delay=0.1):
    text_width = len(text) * 8
    clear_display()
    for offset in range(text_width + 32):  # 32 是为了让文本完全滑出屏幕
        clear_display()
        # 显示文本的每一部分
        for i in range(len(text)):
            char = text[i]
            # 计算字符在屏幕上的起始位置
            char_x = (i * 8) - offset
            if -8 < char_x < 128:  # 只显示在屏幕内的字符
                matrix.text(char, char_x, 0, 1)
        matrix.show()
        sleep(delay)

# 运行跑马灯程序
try:
    while True:
        show_text("Hello, World!")
except KeyboardInterrupt:
    clear_display()
