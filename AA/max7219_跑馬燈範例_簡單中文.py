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

# 翻转字节的函数
def flip_horizontal(byte):
    result = 0
    for i in range(8):
        if (byte & (1 << i)):
            result |= (1 << (7 - i))
    return result

# 修正点阵数据（左右翻转）
CHAR_MAP = {
    '中': [flip_horizontal(0x10), flip_horizontal(0x10), flip_horizontal(0xFE), flip_horizontal(0x92), flip_horizontal(0xFE), flip_horizontal(0x10), flip_horizontal(0x10), flip_horizontal(0x00)],
    '正': [flip_horizontal(0x3E), flip_horizontal(0x08), flip_horizontal(0x08), flip_horizontal(0x0E), flip_horizontal(0x28), flip_horizontal(0x28), flip_horizontal(0x7E), flip_horizontal(0x00)],
    '大': [flip_horizontal(0x10), flip_horizontal(0x10), flip_horizontal(0xFE), flip_horizontal(0x10), flip_horizontal(0x10), flip_horizontal(0x28), flip_horizontal(0x46), flip_horizontal(0x00)],
    '一': [flip_horizontal(0x00), flip_horizontal(0x00), flip_horizontal(0x00), flip_horizontal(0x7E), flip_horizontal(0x00), flip_horizontal(0x00), flip_horizontal(0x00), flip_horizontal(0x00)]
}

# 清除显示
def clear_display():
    matrix.fill(0)
    matrix.show()

# 显示 8x8 点阵数据
def show_char(char):
    if char not in CHAR_MAP:
        return  # 不支持的字符
    data = CHAR_MAP[char]
    matrix.fill(0)
    for y in range(8):
        for x in range(8):
            if data[y] & (1 << x):
                matrix.pixel(x, y, 1)
    matrix.show()
    sleep(0.5)  # 显示速度调整

# 显示文本
def show_text(text):
    text_width = len(text) * 8
    for offset in range(text_width + 32):  # 32 是为了让文本完全滑出屏幕
        clear_display()
        for i, char in enumerate(text):
            if char in CHAR_MAP:
                char_data = CHAR_MAP[char]
                char_x = (i * 8) - offset
                if -8 < char_x < 128:  # 只显示在屏幕内的字符
                    for y in range(8):
                        row = char_data[y]
                        for x in range(8):
                            if row & (1 << x):
                                matrix.pixel(char_x + x, y, 1)
        matrix.show()
        sleep(0.1)  # 调整滚动速度

# 运行显示程序
try:
    while True:
        show_text("中正大一")
except KeyboardInterrupt:
    clear_display()
