# OK-Presenter -- OK:ESP32 BLE-HID Example
# (C) 2023 WiFiBoy Computing Laboratory Taiwan
#
# upload and rename to main.py to run this at boot time
# please also upload hid_services.py to flash disk before running
#
# get hid_services.py from https://github.com/Heerkog/MicroPythonBLEHID

from hid_services import Keyboard

_key_list = {
    1:  0x11, # Button_A:     forward
    2:  0x13, # Button_B:     backward
    4:  0x05, # Button_Right: blank screen
    8:  0x29, # Button_Left:  stop presentation
    16: 0x4d, # Button_Down:  end last slide
    32: 0x4a, # Button_Up:    home first slide
    64: 0x3e, # Button_MENU:  start presentation (F5)
}
    
class HIDDevice:
    def __init__(self):
        self.keyboard = Keyboard("OK:ESP32")
        self.keyboard.set_state_change_callback(self.keyboard_state_callback)
        self.keyboard.start_advertising()
        self.keyboard.set_bonding(True)
        self.keyboard.set_le_secure(True)
        self.keyboard.start()

    def keyboard_state_callback(self): return
    def keyboard_event_callback(self, bytes): return
    def press_key(self, key):
        self.keyboard.set_keys(key)
        self.keyboard.notify_hid_report()
        time.sleep(0.01)
        self.keyboard.set_keys(0x00)
        self.keyboard.notify_hid_report()
    def ok_key(self):
        key = wb.getkey()
        if key!=0:
            if self.keyboard.get_state() is Keyboard.DEVICE_CONNECTED:
                self.press_key(_key_list[key])
            else: print('not connected')
            while wb.getkey()==key: pass
    def start(self):
        while True:
            if self.keyboard.get_state() is Keyboard.DEVICE_IDLE:
                self.keyboard.start_advertising()
            self.ok_key()
            time.sleep(0.1)
           
if __name__ == "__main__":
    okpresenter = HIDDevice()
    okpresenter.start()
