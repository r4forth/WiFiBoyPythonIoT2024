from ir_rx.nec import NEC_16
from machine import Timer
from machine import Pin

def callBack(data, addr, ctrl):
    global _data, _addr
    _data = ir_key[data]
    _addr = addr
    if data > 0:
        print("data: {:02x} addr: {:04x}".format(data, addr))
        print(_data)

ir = NEC_16(Pin(2, Pin.IN), callBack)

ir_key = {
    0x12 : 'Power',
    0x1a : 'Mute',
    0x1e : 'Favorite',
    0x01 : '1',
    0x02 : '2',
    0x03 : '3',
    0x04 : '4',
    0x05 : '5',
    0x06 : '6',
    0x07 : '7',
    0x08 : '8',
    0x09 : '9',
    0x1b : '0',
    0x0a : 'Vol_up',
    0x0c : 'Vol_down',
    0x1f : 'CH_up',
    0x0e : 'CH_down',
    0x0d : 'Full Screen'   
}

_data = 0
if _data == '1':
    wb.cls()
elif _data == '2':
    wb.str('Press 2!', 20, 30, 4)