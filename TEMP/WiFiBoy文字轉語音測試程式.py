import time
import machine
import lib.syn6988
# WiFiBoy 接腳
# GND   ---> GND
# 3V3   ---> 3V3
# IO2   ---> RDY  
# IO5   ---> TX
# IO21  ---> RX
### setup device
ser = machine.UART(
    2, baudrate=9600, bits=8, parity=None, stop=1, tx=5, rx=21
)

busyPin = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
s = lib.syn6988.SYN6988(ser, busyPin)

def speak_and_spell(r):
    # print then speak string r
    s.speak(r)
    return s

# 選擇 語言
lang = 1
# str = "call 13811002200"
# speak_and_spell(str)

# str2 = "[g1]2012-05-01 10:36:28"
# speak_and_spell(str2)

# str3 = "[x1]sound112[m3][g1][v6][n2][i1][y1][f0][b1]2021一，鄧小平"
# a = speak_and_spell(str3)
# print(a)

#
str4 = ""
speak_and_spell(str4)
print(a)
# 警告聲
# Warn_snd_str = "[x1]sound112" 
# print(Warn_snd_str)
# s.speak(Warn_snd_str)
# time.sleep(2)
#         

# for r in ((101, 124), (201, 209), (301, 318), (401, 408)):
#     for s in range(r[0], r[1]+1):
#         playstr = "[x1]sound%3d" % s
#         print(playstr)
#         sp.speak(playstr)
#         time.sleep(2)


# speak_and_spell(
#     "[g2]Hello! WiFiBoy[g1]你好![g2]"
# )  # language selection with [g*]
# speak_and_spell("I can speak in English, and also in Chinese:")
# speak_and_spell("[g1]千里之行，始于足下。[g2]")
# speak_and_spell(
#     "which means: a journey of five hundred kilometres starts with the first step"
# )