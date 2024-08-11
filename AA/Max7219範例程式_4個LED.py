from machine import Pin, SPI
import lib.max7219
from utime import sleep
# WiFiBoy PythonIoT    max7219 8x8 LED Matrix
# 5V               --> VCC
# GND              --> GND
# GPIO 23 MOSI     --> DIN
# GPIO  5 CS       --> CS
# GPIO 18 SCK      --> CLK  
CLOCK_PIN = 18
DATA_PIN = 23
CS_PIN = 5

# 初始化 SPI，SPI 1 已經被 LCD 使用
spi0 = SPI(2, baudrate=10000000, polarity=0, phase=0, sck=Pin(CLOCK_PIN), mosi=Pin(DATA_PIN))

# 初始化 Chip Select 引脚
cs = Pin(CS_PIN, Pin.OUT)

# 初始化 MAX7219 LED 矩阵，如果只接 1 個 LCD，將 4 改成 1
display = lib.max7219.Matrix8x8(spi0, cs, 4)

# 显示文本 '1234' 从位置 (0, 0)，亮灯
# display.text 用法: 參數1 傳入的字串、參數2 參數2 參數4: 開燈 1 / 關燈 0 
# display.text('1234', 5, 5, 1)
# display.show()
# display.pixel(0,0,1)
# display.pixel(1,1,1)
# display.hline(0,4,8,1)
# display.vline(4,0,8,1)
# display.line(8, 0, 16, 8, 1)
# display.rect(17,1,6,6,1)
# display.fill_rect(25,1,6,6,1)
# display.show()




delay_time = 1
while True:
    # Draw a single character

    display.text('A', 0, 0, 1)
    display.show()
    sleep(delay_time)

    # Draw an X in a box
    display.fill(0)
    display.line(0, 0, 7, 7, 1)
    display.show()
    sleep(delay_time)

    display.line(7, 0, 0, 7, 1)
    display.show()
    sleep(delay_time)

    display.rect(0, 0, 8, 8, 1)
    display.show()
    sleep(delay_time)
    display.fill(0)

    # Smile Face
    display.pixel(1, 1, 1)
    display.pixel(6, 1, 1)
    display.pixel(0, 4, 1)
    display.pixel(7, 4, 1)
    display.pixel(1, 5, 1)
    display.pixel(6, 5, 1)
    display.pixel(2, 6, 1)
    display.pixel(5, 6, 1)
    display.pixel(3, 7, 1)
    display.pixel(4, 7, 1)
    display.show()
    sleep(delay_time)
    display.fill(0)
    display.show()
    (delay_time)

# 进入无限循环前的延时
# sleep(2)  # 确保显示数据有时间展示

# 无限循环，防止 WDT 重启
# while True:
#     sleep(1)  # 避免过度占用 CPU
