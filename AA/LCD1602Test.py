import time
from machine import SoftI2C, Pin
from lib.esp32_i2c_1602lcd import I2cLcd


DEFAULT_I2C_ADDR = 0x27
i2c = SoftI2C(sda=Pin(23),scl=Pin(22),freq=100000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)

for i in range(1, 10):
    lcd.clear()
    lcd.putstr("loading...{}\n".format(i))
    lcd.putstr("Hi! WiFiBoy.")
    time.sleep(1)