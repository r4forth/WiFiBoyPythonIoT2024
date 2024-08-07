import machine
import time
from machine import Pin
import uhid

# 初始化 USB HID 设备
hid = uhid.HID()

# 定义一个函数来发送按键事件
def send_key(key_code):
    # 创建一个 HID 报告
    report = bytearray(8)
    report[0] = 0  # 使用报告ID 0
    report[2] = key_code  # 设置按键码
    hid.send_report(report)
    time.sleep(0.1)  # 等待 100 毫秒
    report[2] = 0  # 释放按键
    hid.send_report(report)

# 主程序循环
while True:
    # 发送 'A' 键
    send_key(0x04)  # 'A' 的 HID 键码
    time.sleep(1)  # 每隔 1 秒发送一次
