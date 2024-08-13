from machine import Pin
import time
from machine import PWM
from time import sleep_ms

def draw_squares():
    # 設定正方形的邊長和步長
    step = 10
    start_x = 0
    start_y = 0
    
    # 清除屏幕
    wb.cls(0)
    
    # 在 120x120 的範圍內畫出空心正方形
    for size in range(120, 0, -step):
        x1 = start_x
        y1 = start_y
        x2 = start_x + size
        y2 = start_y + size
        
        # 確保正方形在範圍內
        if x2 > 120:
            x2 = 120
        if y2 > 120:
            y2 = 120
        
        # 畫正方形的四條邊
        wb.line(x1, y1, x2, y1, wb.BLUE)  # 上邊
        wb.line(x1, y1, x1, y2, wb.BLUE)  # 左邊
        wb.line(x2, y1, x2, y2, wb.BLUE)  # 右邊
        wb.line(x1, y2, x2, y2, wb.BLUE)  # 下邊


# 繪製正方形
draw_squares()
