import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

def test_main():
    # Test function for verifying LCD1602 full character set
    print("Running LCD1602 full character set")
    
    # 初始化 I2C
    i2c = I2C(0, sda=Pin(23), scl=Pin(22), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    
    lcd.backlight_on()
    lcd.clear()
    
    # LCD1602 支援的符號
    lcd_chars = []
    
    # 增加自己定義的符號 (0x00 至 0x07)
    for x in range(0x00, 0x08):
        lcd_chars.append(chr(x))
    
    # 增加標準 ASCII 符號(0x20 至 0x7F)
    for x in range(0x20, 0x80):
        lcd_chars.append(chr(x))
    
    char_string = ''.join(lcd_chars)
    print("Displaying all supported characters.")
    
    # 依次顯示字符
    for i in range(0, len(char_string), I2C_NUM_COLS):
        lcd.clear()
        lcd.putstr(char_string[i:i + I2C_NUM_COLS])
        time.sleep(1)  # 每秒更新一次

# 執行程式
test_main()
