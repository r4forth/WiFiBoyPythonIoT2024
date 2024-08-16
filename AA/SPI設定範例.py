import os
from machine import Pin, SoftSPI
from sdcard import SDCard
# MISO GPIO19 PIN 7
# MOSI GPIO23 PIN 10
# CS   GPIO5  PIN5           ChipSelect
# SCK  GPIO18 PIN 8 CLOCK    VSPI CLK
# 預設設定
spisd = SoftSPI(2, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
sd = SDCard(spisd, Pin(5))
# ===========================================================
## 01. 印出根目錄檔案清單
# print('/lib/: {}'.format(os.listdir('lib')))
# ===========================================================
# # 02. 掛載 SDCard
# vfs = os.VfsFat(sd)
# os.mount(vfs, '/sd')
# os.chdir('sd')
# print('SD 卡的根目錄:{}'.format(os.listdir()))
# print('===================================================')
# ===========================================================
# # 03. 開啟 cmdline.txt 檔案，查看裡面內容
# vfs = os.VfsFat(sd)
# os.mount(vfs, '/sd')
# os.chdir('sd')
# f = open('cmdline.txt', 'r')
# print('cmdline.txt 的檔案內容:')
# print('===========================================')
# print(f.read())
# f.close()
# print('===========================================')

## 04. 建立一個檔案並增加內容:
# vfs = os.VfsFat(sd)
# os.mount(vfs, '/sd')
# os.chdir('sd')
# f = open('WiFiBoyFiles.txt', 'w')
# f.write('Hello, WiFiBoy!')
# f.close()

## 05. 附加檔案到 WiFiBoyFiles.txt:
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
os.chdir('sd')
f = open('WiFiBoyFiles.txt', 'a')
f.write('參加 2024 ITHome 鐵人賽!')
f.close()

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