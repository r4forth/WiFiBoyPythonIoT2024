# SD 卡讀取範例
# WiFiBoy 對應的 SPI 腳位
# MISO GPIO19 --> 要接在 WiFiBoy 的腳位 PIN 7    
# MOSI GPIO23 --> 要接在 WiFiBoy 的腳位 PIN 10
# SCK  GPIO18 --> 要接在 WiFiBoy 的腳位 PIN 8
# CS   GPIO5  --> 要接在 WiFiBoy 的腳位 PIN 5

# 初始化 SPI 接口
from machine import Pin, SoftSPI
import os
from lib.sdcard import sdcard

# import os
# from machine import Pin, SoftSPI
# from sdcard import SDCard
spisd = SoftSPI(1, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
sd = sdcard(spisd, Pin(5))

print('Root directory:{}'.format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
# print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')
print('SD Card contains:{}'.format(os.listdir()))


# 1. To read file from the root directory:
# f = open('sample.txt', 'r')
# print(f.read())
# f.close()

# 2. To create a new file for writing:
# f = open('sample2.txt', 'w')
# f.write('Some text for sample 2')
# f.close()

# 3. To append some text in existing file:
# f = open('sample3.txt', 'a')
# f.write('Some text for sample 3')
# f.close()

# 4. To delete a file:
# os.remove('file to delete')

# 5. To list all directories and files:
# os.listdir()

# 6. To create a new folder:
# os.mkdir('sample folder')

# 7. To change directory:
# os.chdir('directory you want to open')

# 8. To delete a folder:
# os.rmdir('folder to delete')

# 9.  To rename a file or a folder:
# os.rename('current name', 'desired name')

# # Assign chip select (CS) pin (and start it high)
# cs = machine.Pin(8, machine.Pin.OUT)
# # Intialize SPI peripheral (start with 1 MHz)
# spi = machine.SPI(2,
#                   baudrate=1000000,
#                   polarity=0,
#                   phase=0,
#                   bits=8,
#                   firstbit=machine.SPI.MSB,
#                   sck=machine.Pin(6),
#                   mosi=machine.Pin(10),
#                   miso=machine.Pin(7))
# # Initialize SD card
# sd = sdcard.SDCard(spi, cs)
# 
# # OR this simpler initialization code should works on Maker Pi Pico too...
# #sd = sdcard.SDCard(machine.SPI(1), machine.Pin(15))
# 
# os.mount(sd, '/sd')
# # check the content
# os.listdir('/sd')
# 
# # try some standard file operations
# file = open('/sd/test.txt', 'w')
# file.write('Testing SD card on Maker Pi Pico')
# file.close()
# file = open('/sd/test.txt', 'r')
# data = file.read()
# print(data)
# file.close()
# 
# 
# # 接线说明:
# # MISO GPIO19 PIN 7
# # MOSI GPIO23 PIN 10
# # SCK  GPIO2  PIN 4
# # CS   GPIO18 PIN 8
# 
# spisd=machine.SPI(2, miso=machine.Pin(7), mosi=machine.Pin(10), sck=machine.Pin(4))
# sd=SDCard(spisd, machine.Pin(8))
# 
# print('未挂载SD之前:{}'.format(os.listdir()))
# 
# vfs=os.VfsFat(sd)
# os.mount(vfs,'/sd')
# 
# print('挂载SD开之后:{}'.format(os.listdir()))
# 
# os.chdir('sd')
# 
# print('SD卡中的文件:{}'.format(os.listdir()))
# 
# with open("/sd/test.txt", "w") as f:
#     for i in range(1, 101):
#         f.write(str(i)+"\n")
# 
# print("已经将1 2 3....100写入到SD卡中的text.txt文件")