# 05_04. 當按下 A 鍵，畫面上的計數器加一
from machine import Pin
from time import sleep
Counter = 0
Limit = 120
STEP = 1
print('請觀察: 觀看正面計數器的值: ')
wb.cls(wb.BLACK)
while True:
    if wb.getkey() == 2:
        wb.cls()
        time.sleep(0.1)
        Counter = Counter + STEP
        if Counter >= Limit:
            wb.str('Finish!', 16, 64, 2, 4)
            break
        wb.str(str(Counter), 16, 64, 2, 5)

        