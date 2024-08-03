from time import sleep
import math

angle = 0
Radius = 1
while True:
    rad = math.radians(angle)
    sin_arc = math.sin(rad)
    y = round((Radius * sin_arc), 3)
    print(-1.5, y, 1.5)
    sleep(0.05)
    angle = angle + 10
    if angle >= 360:
        angle = 0
    