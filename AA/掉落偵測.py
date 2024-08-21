from machine import Pin
from utime import sleep



while True:
    center = Pin(2, Pin.IN, Pin.PULL_DOWN)
    print(center.value())
    if center.value() == 1:
        wb.cls()
        wb.str("Dangerous!", 10, 20, 5)
    else:
        wb.cls()
    sleep(1)
