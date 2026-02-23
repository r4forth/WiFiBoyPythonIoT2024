from machine import Pin
import wb_config
from utime import sleep



while True:
    center = Pin(wb_config.Pins.IR_RECEIVER, Pin.IN, Pin.PULL_DOWN)
    print(center.value())
    if center.value() == 1:
        wb.cls()
        wb.str("Dangerous!", 10, 20, 5)
    else:
        wb.cls()
    sleep(1)
