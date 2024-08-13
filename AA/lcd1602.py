from machine import I2C, Pin
import time

class LCD1602:
    def __init__(self, i2c, address=0x27):
        self.i2c = i2c
        self.address = address
        self.init_display()

    def send_command(self, cmd):
        self.i2c.writeto(self.address, bytearray([0x80, cmd]))
        time.sleep_ms(1)

    def send_data(self, data):
        self.i2c.writeto(self.address, bytearray([0x40, data]))
        time.sleep_ms(1)

    def init_display(self):
        self.send_command(0x33)  # 初始化
        time.sleep_ms(5)
        self.send_command(0x32)  # 设置为 4 位模式
        time.sleep_ms(5)
        self.send_command(0x28)  # 2 行，5x7 点阵
        time.sleep_ms(5)
        self.send_command(0x0C)  # 开显示，不显示光标
        time.sleep_ms(5)
        self.send_command(0x06)  # 文字不移动
        time.sleep_ms(5)
        self.clear()

    def clear(self):
        self.send_command(0x01)  # 清屏
        time.sleep_ms(2)

    def puts(self, string, line=0, col=0):
        if line == 0:
            addr = col
        elif line == 1:
            addr = 0x40 + col
        else:
            return
        self.send_command(0x80 | addr)
        for char in string:
            self.send_data(ord(char))