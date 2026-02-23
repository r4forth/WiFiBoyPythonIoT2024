from machine import Pin
import wb_config
from utime import sleep

# 初始化紅外線感測器的引腳
left_sensor = Pin(wb_config.Pins.IR_RECEIVER, Pin.IN)    # 左側感測器連接到 GPIO 2
center_sensor = Pin(wb_config.Pins.SPI_CS, Pin.IN)  # 中間感測器連接到 GPIO 5
right_sensor = Pin(wb_config.Pins.SYN6988_BUSY, Pin.IN)   # 右側感測器連接到 GPIO 21

def read_sensors():
    left = left_sensor.value()
    center = center_sensor.value()
    right = right_sensor.value()
    return left, center, right

def check_track():
    left, center, right = read_sensors()
    if center == 1 and left == 0 and right == 0:
        print("AGV 運行正常")
    elif left == 1 and center == 0:
        print("AGV 偏離軌道: 要往右調整")
    elif right == 1 and center == 0:
        print("AGV 偏離軌道: 要往左調整")
    else:
        print("AGV 脫離軌道")

while True:
    check_track()
    sleep(0.1)
