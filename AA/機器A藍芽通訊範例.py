import ubluetooth
import time

class ESP32_Bluetooth:
    def __init__(self):
        self.bt = ubluetooth.BLE()
        self.bt.active(True)
        self.bt.irq(self.bt_irq)
        self.scan_results = None
        self.conn = None

    def bt_irq(self, event, data):
        if event == 1:  # BLE.IRQ_SCAN_RESULT
            addr_type, addr, adv_type, rssi, adv_data = data
            if b'WiFiBoy_B' in adv_data:  # 找到機器B
                self.scan_results = addr
                self.bt.gap_scan(None)  # 停止掃描
        elif event == 7:  # BLE.IRQ_PERIPHERAL_CONNECT
            self.conn = data
        elif event == 8:  # BLE.IRQ_PERIPHERAL_DISCONNECT
            self.conn = None

    def scan(self):
        self.bt.gap_scan(2000, 30000, 30000)  # 開始掃描2秒

    def connect(self):
        if self.scan_results:
            self.bt.gap_connect(0, self.scan_results)

    def send_message(self, message):
        if self.conn:
            self.bt.gattc_write(self.conn, 0x0010, message.encode('utf-8'), 1)

    def receive_message(self):
        if self.conn:
            return self.bt.gattc_read(self.conn, 0x0010)

    def close(self):
        if self.conn:
            self.bt.gap_disconnect(self.conn)

# 程序執行
bt_a = ESP32_Bluetooth()

bt_a.scan()
time.sleep(2)
bt_a.connect()
time.sleep(1)
bt_a.send_message("你好!我是玩學機A，請問你是誰?")

while True:
    received = bt_a.receive_message()
    if received:
        print("收到:", received)
        response = input("輸入訊息發送給B：")
        bt_a.send_message(response)
