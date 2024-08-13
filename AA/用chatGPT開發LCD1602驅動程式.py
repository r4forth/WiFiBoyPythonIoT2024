# 用 ChatGPT 開發 LCD1602 的驅動程式
import time
from machine import I2C, Pin
from lib.lcd1602 import LCD1602

# 使用 I2C 1，SCL=Pin(22)，SDA=Pin(23)
# i2c = SoftI2C(sda=Pin(23),scl=Pin(22),freq=100000)
i2c = I2C(1, sda=Pin(23), scl=Pin(22),  freq=100000)
lcd = LCD1602(i2c)

# 测试代码
lcd.clear()
lcd.puts("A", 0, 0)