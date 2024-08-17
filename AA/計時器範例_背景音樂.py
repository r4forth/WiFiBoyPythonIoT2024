import toneng
import random
import utime
from machine import Timer

# 設定定時器
BGM_Timer = Timer(0)
CleanScreen_Timer = Timer(1)
ShowString_Timer = Timer(2)
wb.cls()
def play_music(timer):
    utime.sleep_ms(10)  # 增加轻微延迟
    start_time = utime.ticks_ms()
    toneng._ps = "O3CDECCDECEFG2EFG2G8A8G8F8ECG8A8G8F8ECDO2GO3C2DO2GO3C2"
    print("play_music took", utime.ticks_diff(utime.ticks_ms(), start_time), "ms")

def CleanScreen(timer):
    utime.sleep_ms(10)  # 增加轻微延迟
    start_time = utime.ticks_ms()
    # wb.cls(random.randint(0, 10))
    wb.cls()
    print("CleanScreen took", utime.ticks_diff(utime.ticks_ms(), start_time), "ms")

def ShowString(timer):
    utime.sleep_ms(10)  # 增加轻微延迟
    start_time = utime.ticks_ms()
    wb.str('WiFiBoy!', random.randint(0, 160), random.randint(0, 120), 2, 1)
    print("ShowString took", utime.ticks_diff(utime.ticks_ms(), start_time), "ms")
    
    
BGM_Timer.init(period=10000, mode=Timer.PERIODIC, callback=play_music)
# CleanScreen_Timer.init(period=9000, mode=Timer.PERIODIC, callback=CleanScreen)
# ShowString_Timer.init(period=1000, mode=Timer.PERIODIC, callback=ShowString)
