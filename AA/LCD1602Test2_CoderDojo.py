import utime
import wb_config
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

def test_main():
    #Test function for verifying basic functionality
    print("Running test_main")
    i2c = I2C(0, sda=machine.Pin(wb_config.Pins.I2C_SDA), scl=machine.Pin(wb_config.Pins.I2C_SCL), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
    count = 0
    lcd.backlight_on()
     
    lcd.clear()
    string = ""
    for x in range(32, 32+I2C_NUM_ROWS*I2C_NUM_COLS):
        string += chr(x)
    print("String: ", string)
    lcd.putstr(string)

test_main()
