from machine import Pin
from machine import UART

def main():
    # UART 1設成USB序列埠的預設腳
    com = UART(1, 9600, tx=1, rx=3)
    com.init(9600)
    led = Pin(16, Pin.OUT, value=1)

    while True:
        choice = com.readline()

        if choice == b'LED_ON\n':
            led.value(0)
            com.write(b'LED is ON!\n')  # 回應訊息給電腦端的Python
        elif choice == b'LED_OFF\n':
            led.value(1)
            com.write(b'LED is OFF!\n')

if __name__ == '__main__':
    ser_pin = Pin(13, Pin.IN, Pin.PULL_UP) # 腳13設成輸入、啟用上拉電阻。
    if ser_pin.value() == 1:  # 若腳13沒有接地…
        main()