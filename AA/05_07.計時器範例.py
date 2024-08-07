# 05_07. 計時器範例
from machine import Timer, Pin
from time import localtime

# 設置內建LED
led = Pin(16, Pin.OUT)

# 初始化 LED 狀態
led_state = False
runtime = 0  # 用於計算運行時間的變數
wb.cls()
wb.str('Program Start!', 2, 64, 2, 2)

# 定義第一個計時器的中斷處理函數，用於每 10 秒印出時間
def print_time(timer):
    current_time = localtime()  # 取得當前時間
    H = str(f"{current_time[3]:02}")
    M = str(f"{current_time[4]:02}")
    S = str(f"{current_time[5]:02}")
    wb.cls()
    wb.str("Current Time: ", 2, 64, 2, 2)
    wb.str(H + " : " + M + " : " + S, 2, 80, 2, 2)
# 定義第二個計時器的中斷處理函數，用於每 5 秒切換LED
def toggle_led(timer):
    global led_state
    led_state = not led_state
    led.value(led_state)

# 定義第三個計時器的中斷處理函數，用於計算總運行時間並結束程式
def check_runtime(timer):
    global runtime
    runtime += 1
    if runtime >= 120:  # 如果運行時間超過120秒（2分鐘）
        print("Program finished running for 2 minutes.")
        wb.str('Program End!', 2, 64, 2, 2)
        timer1.deinit()
        timer2.deinit()
        timer3.deinit()

# 創建第一個計時器，每 10 秒觸發一次
timer1 = Timer(0)
timer1.init(period=10000, mode=Timer.PERIODIC, callback=print_time)

# 創建第二個計時器，每 5 秒觸發一次
timer2 = Timer(1)
timer2.init(period=5000, mode=Timer.PERIODIC, callback=toggle_led)

# 創建第三個計時器，每 1 秒更新一次運行時間
timer3 = Timer(2)
timer3.init(period=1000, mode=Timer.PERIODIC, callback=check_runtime)