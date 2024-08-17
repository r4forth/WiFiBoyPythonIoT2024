# 蜂鳴器範例.py

from machine import Pin, PWM
from time import sleep

# 蜂鳴器設定
snd_PinA = Pin(17, 2).value(1)
snd_PinB = Pin(25, 2)
snd = PWM(snd_PinB)

# tones = {
# "A2": 110,"AS2": 117,"B2": 123,"C3": 131,"CS3": 139,
# "D3": 147,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,"G3": 196,"GS3": 208,"A3": 220,"AS3": 233,"B3": 247,
# "C4": 262,"CS4": 277,"D4": 294,"DS4": 311,"E4": 330,"F4": 349,"FS4": 370,"G4": 392,"GS4": 415,"A4": 440,"AS4": 466,"B4": 494,
# "C5": 523,"CS5": 554,"D5": 587,"DS5": 622,"E5": 659,"F5": 698,
# "FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,
# "C6": 1047,"CS6": 1109,"D6": 1175,"DS6": 1245,"E6": 1319,"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,
# "A6": 1760,"AS6": 1865,"B6": 1976,
# "C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,"F7": 2794,"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,"AS7": 3729,"B7": 3951,
# "C8": 4186,"CS8": 4435,"D8": 4699,"DS8": 4978
# }
# 
# 
# 
# 發聲程式
def play(freq, t):
    snd.duty(80)
    snd.freq(freq)
    sleep(t)
    snd.duty(0)
#     
# # 01. 發出單音 Do C4
# play(262, 1)
# snd.deinit()
# 
# # 02. 播放音階 Do Mi So 三次
# i = 0
# while  i < 3:
#     play(262, 1)
#     play(330, .5)
#     play(392, .5)
#     i = i + 1
# snd.deinit()



# # 04. 使用內建音掉引擎，撥放音樂
import toneng, time
# 預設 C3 第三區
ps1 = "CDEFGABC"
ps2 = "GEEFDD2"
ps3 = "ABCDEFG"
ps = [ps1, ps2, ps3]

# 先撥放第一段，再撥放第二段
for i in range(len(ps)):
    toneng._ps = ps[i]
    print(i)
    sleep(2)