# 讀取 WiFiBoy 內建的三軸加速度計
# Micropython Example: Reading OKESP32Pro 3D Accelerometer (LIS3DH)
# (C)2024 WiFiBoy Computing Laboratory Taiwan

import machine, time

i2c=machine.SoftI2C(scl=machine.Pin(22),sda=machine.Pin(23)) 
i2c.writeto_mem(0x19,0x20,b'\x77')
i2c.writeto_mem(0x19,0x23,b'\x88')

def twosComp(x):
    if (0x8000 & x): x = - (0x010000 - x)
    return x

def get_x():
    n1 = i2c.readfrom_mem(0x19, 0x2A, 1)
    n2 = i2c.readfrom_mem(0x19, 0x2B, 1)
    x = twosComp(n1[0]+n2[0]*256)/16380
    return x

def get_y():
    n1 = i2c.readfrom_mem(0x19, 0x28, 1)
    n2 = i2c.readfrom_mem(0x19, 0x29, 1)
    y = twosComp(n1[0]+n2[0]*256)/16380
    return -y

def get_z():
    n1 = i2c.readfrom_mem(0x19, 0x2C, 1)
    n2 = i2c.readfrom_mem(0x19, 0x2D, 1)
    z = twosComp(n1[0]+n2[0]*256)/16380
    return z

while True:
    dx = get_x()
    dy = get_y()
    dz = get_z()
    print(dx, dy, dz)
    time.sleep(0.01)
