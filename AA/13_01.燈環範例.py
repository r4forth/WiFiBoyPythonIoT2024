# # 燈環範例
#
# 13.01 產生一組紅綠燈，紅燈顯示在11位置，黃燈顯示在0位置，綠燈顯示在1位置。
# import time
# from machine import Pin
# from neopixel import NeoPixel
# LED_RED = (64, 0, 0)
# LED_GREEN = (0, 64, 0)
# LED_BLUE = (0, 0, 64)
# LED_YELLOW = (64, 64, 0)
# pin = Pin(2, Pin.OUT)    
# np = NeoPixel(pin, 12)
# # 亮紅綠燈
# np[11] =  LED_RED
# np[0] =  LED_YELLOW
# np[1] =  LED_GREEN
# np.write() 

# # 13.02 產生一個紅燈，每隔一秒繞著燈環跑
# import time
# from machine import Pin
# from neopixel import NeoPixel
# 
# pin = Pin(2, Pin.OUT)    
# np = NeoPixel(pin, 12)   
# for i in range(0, 12):   
#     np[i] = (0, 64, 0) 
#     np.write()            
#     time.sleep(1)
#     np[i] = (0, 0, 0) 
#     np.write()


# 13.03 寫一個紅綠燈模擬程式
# import time
# from machine import Pin
# from neopixel import NeoPixel
# pin = Pin(2, Pin.OUT)    
# np = NeoPixel(pin, 12)
# # 主程式
# def set_light(red, yellow, green):
#     """設定紅綠燈的顏色"""
#     np[11] = (red, 0, 0)    # 紅燈
#     np[0] = (yellow, yellow, 0)  # 黃燈
#     np[1] = (0, green, 0)  # 綠燈
#     np.write()
# 
# while True:
#     # 紅燈亮 10 秒
#     for i in range(8):
#         set_light(255, 0, 0)  # 紅燈亮，黃燈和綠燈關
#         time.sleep(1)
#     
#     # 第8秒時黃燈開始閃爍，紅燈保持亮
#     for i in range(4):
#         set_light(255, 255, 0)  # 紅燈和黃燈亮
#         time.sleep(0.5)
#         set_light(255, 0, 0)    # 紅燈亮，黃燈關
#         time.sleep(0.5)
# 
#     # 綠燈亮 8 秒
#     for i in range(6):
#         set_light(0, 0, 255)  # 綠燈亮，紅燈和黃燈關
#         time.sleep(1)
# 
#     # 第6秒時綠燈開始閃爍
#     for i in range(4):
#         set_light(0, 0, 255)  # 綠燈亮
#         time.sleep(0.5)
#         set_light(0, 0, 0)    # 所有燈都關
#         time.sleep(0.5)
#     # 迴圈結束後自動回到紅燈狀態

# 13.04 電子色子模擬程式
# 彩燈骰子
import time
import neopixel
# 蜂鳴器啟動
machine.Pin(17, 2).value(1)
snd = machine.PWM(machine.Pin(25,2))
snd.duty(0)

def play(f, t):
    snd.freq(f); snd.duty(50)
    time.sleep(t); snd.duty(0)

# 燈環控制
numbers = 12
np = neopixel.NeoPixel(machine.Pin(2), numbers, bpp = 3)
print('請按任一鍵開始丟骰子!')
wb.cls()
while True:
    if wb.getkey() > 0:
        count = wb.rand() % 100 + 20
        for i in range(1, count):
            np[i%numbers] = (64, 0, 0)
            play(880, 0.02)
            np.write()
            wb.str(str(i%numbers), 10, 20, 2, 15)
            if i == count-1:
                print('')
            else:
                wb.cls()
            np[i%numbers] = (0, 0, 0)
            time.sleep(0.01)


