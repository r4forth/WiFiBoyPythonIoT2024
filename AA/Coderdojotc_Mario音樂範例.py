from machine import Pin, PWM
from time import sleep

# 蜂鳴器設定
snd_PinA = Pin(17, 2).value(1)
snd_PinB = Pin(25, 2)
snd = PWM(snd_PinB)

tones = {
"A2": 110,"AS2": 117,"B2": 123,"C3": 131,"CS3": 139,
"D3": 147,"DS3": 156,"E3": 165,"F3": 175,"FS3": 185,"G3": 196,"GS3": 208,"A3": 220,"AS3": 233,"B3": 247,
"C4": 262,"CS4": 277,"D4": 294,"DS4": 311,"E4": 330,"F4": 349,"FS4": 370,"G4": 392,"GS4": 415,"A4": 440,"AS4": 466,"B4": 494,
"C5": 523,"CS5": 554,"D5": 587,"DS5": 622,"E5": 659,"F5": 698,
"FS5": 740,"G5": 784,"GS5": 831,"A5": 880,"AS5": 932,"B5": 988,
"C6": 1047,"CS6": 1109,"D6": 1175,"DS6": 1245,"E6": 1319,"F6": 1397,"FS6": 1480,"G6": 1568,"GS6": 1661,
"A6": 1760,"AS6": 1865,"B6": 1976,
"C7": 2093,"CS7": 2217,"D7": 2349,"DS7": 2489,"E7": 2637,"F7": 2794,"FS7": 2960,"G7": 3136,"GS7": 3322,"A7": 3520,"AS7": 3729,"B7": 3951,
"C8": 4186,"CS8": 4435,"D8": 4699,"DS8": 4978}

def playtone(frequency):
    snd.duty(50)
    snd.freq(frequency)

def bequiet():
    snd.duty(0)
    
def playsong(mysong):
    for i in range(len(mysong)):
        if (mysong[i] == "P" or mysong[i] == 0 ):
            bequiet()
        else:
            playtone(tones[mysong[i]])
        sleep(0.3)
    bequiet()

mario = ["E5", "E5", 0, "E5", 0, "C5", "E5", 0, "G5", 0, 0, 0, "G4", 0, 0, 0, "C5", 0, 0, "G4",
         0, 0, "E4", 0, 0, "A4", 0, "B4", 0, "AS4", "A4", 0, "G4", "E5", 0, "G5", "A5", 0, "F5", "G5",
         0, "E5", 0,"C5", "D5", "B4", 0, 0, "C5", 0, 0, "G4", 0, 0, "E4", 0, 0, "A4", 0, "B4", 0,
         "AS4", "A4", 0, "G4", "E5", 0, "G5", "A5", 0, "F5", "G5", 0, "E5", 0,"C5", "D5", "B4", 0, 0]
playsong(mario)
snd.deinit()