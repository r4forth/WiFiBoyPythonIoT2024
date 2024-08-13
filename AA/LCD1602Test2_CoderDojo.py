import utime
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
    i2c = I2C(0, sda=machine.Pin(23), scl=machine.Pin(22), freq=400000)
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
