from machine import Pin, PWM
from time import sleep_ms

class BUZZER:
    NOTES = {
        'E7': 2637, 'C7': 2093, 'G7': 3136, 'G6': 1568,
        'E6': 1319, 'A6': 1760, 'B6': 1976, 'AS6': 1865,
        'F7': 2794, 'A7': 3520, 'D7': 2349, 'C6': 1047,
        'B5': 988, 'G5': 784, 'E5': 659, 'C5': 523,
    }

    def __init__(self, sig_pin):
        self.pwm = PWM(Pin(sig_pin, Pin.OUT))
        self.pwm.freq(1)  # Set initial frequency to a very low value
        self.pwm.duty(50)  # Set initial duty cycle to 0

    def play(self, melody, wait, duty):
        for note in melody:
            freq = self.NOTES.get(note, 0)
            if freq > 0:
                self.pwm.freq(freq)
                self.pwm.duty(duty)
            else:
                self.pwm.duty(0)
            sleep_ms(wait)
        self.pwm.duty(0)  # Turn off the sound after the melody ends

def parse_melody(melody_str):
    return melody_str.split()

# 旋律字符串
mario_str = "E7 E7 0 E7 0 C7 E7 0 G7 0 0 0 G6 0 0 0 C7 0 0 G6 0 0 E6 0 0 A6 0 B6 0 AS6 A6 0 G6 E7 0 G7 A7 0 F7 G7 0 E7 0 C7 D7 B6 0 0 C7 0 0 G6 0 0 E6 0 0 A6 0 B6 0 AS6 A6 0 G6 E7 0 G7 A7 0 F7 G7 0 E7 0 C7 D7 B6 0 0"
jingle_str = "E7 E7 E7 0 E7 E7 E7 0 E7 G7 C7 D7 E7 0 F7 F7 F7 F7 F7 E7 E7 E7 E7 D7 D7 E7 D7 0 G7 0 E7 E7 E7 0 E7 E7 E7 0 E7 G7 C7 D7 E7 0 F7 F7 F7 F7 F7 E7 E7 E7 G7 G7 F7 D7 C7 0"
music_str = "B5 0 B5 B5 0 C6 0 0 B5 0 C6 0 B5 0 C6 0 B5 0 B5 B5 B5 0 B5 0 B5 0 B5 0 B5 0 B5 0 G5 0 A5 0 B5 0 B5 0 B5 0 E5 0 G5 0 B5 0 C6 0 F5 0 A5 0 C6 0 E6 0 A5 0 C6 0 E6 0 B5 0 G5 0 A5 0 B5"

# 解析旋律字符串
mario = parse_melody(mario_str)
jingle = parse_melody(jingle_str)
indiana_str = parse_melody(music_str)

# 初始化蜂鸣器对象
snd_PIN = Pin(17, 2).value(1)
buzzer = BUZZER(25)

# print("播放 超级马里奥")
# buzzer.play(mario, 150, 512)
# sleep_ms(1000)
# 
# print("播放 jingle bells.")
# buzzer.play(jingle, 250, 512)
# sleep_ms(1000)
print("播放 星際大戰")
buzzer.play(music_str, 250, 512)
sleep_ms(1000)