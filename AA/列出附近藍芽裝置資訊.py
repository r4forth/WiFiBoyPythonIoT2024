import ubluetooth
from micropython import const
import time

_IRQ_SCAN_RESULT = const(5)

class BLEScanner:
    def __init__(self):
        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.ble.irq(self.ble_irq)
        self.devices = []

    def ble_irq(self, event, data):
        if event == _IRQ_SCAN_RESULT:
            addr_type, addr, adv_type, rssi, adv_data = data
            if addr not in self.devices:
                self.devices.append(addr)
                # 解析廣播數據以提取名稱和其他信息
                device_name = self.extract_device_name(adv_data)
                if device_name:
                    print("Device found:")
                    print("  Name: ", device_name)
                else:
                    print("Unnamed device found:")
                print("  MAC Address: ", self.format_mac(addr))
                print("  RSSI: ", rssi)
                print("-" * 30)

    def start_scan(self, scan_time=10):
        self.devices = []  # 重置已发现设备列表
        print(f"Scanning for {scan_time} seconds...")
        self.ble.gap_scan(scan_time * 1000, 30000, 30000)
        time.sleep(scan_time)
        self.ble.gap_scan(None)
        print("Scan complete.")

    def extract_device_name(self, adv_data):
        length = len(adv_data)
        i = 0
        while i < length:
            if i + 1 >= length:
                return None
            field_length = adv_data[i]
            field_type = adv_data[i + 1]
            if field_length <= 1 or (i + field_length) > length:
                return None
            if field_type == 0x09:  # 完整名稱字段
                return adv_data[i + 2:i + field_length].decode('utf-8', errors='ignore')
            i += field_length
        return None

    def format_mac(self, mac):
        return ':'.join(['{:02X}'.format(b) for b in mac])

# 使用示例
scanner = BLEScanner()
scanner.start_scan(scan_time=20)  # 搜索時間設為10秒
