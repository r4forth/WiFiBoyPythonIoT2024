# 用 ChatGPT 開發 LCD1602 的驅動程式
import time
import wb_config
from machine import I2C, Pin
from lib.lcd1602 import LCD1602

# 使用 I2C 1，SCL=Pin(wb_config.Pins.I2C_SCL)，SDA=Pin(wb_config.Pins.I2C_SDA)
# i2c = SoftI2C(sda=Pin(wb_config.Pins.I2C_SDA),scl=Pin(wb_config.Pins.I2C_SCL),freq=100000)
i2c = I2C(1, sda=Pin(wb_config.Pins.I2C_SDA), scl=Pin(wb_config.Pins.I2C_SCL),  freq=100000)
lcd = LCD1602(i2c)

# 测试代码
lcd.clear()
lcd.puts("A", 0, 0)