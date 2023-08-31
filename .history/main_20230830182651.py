#!/usr/bin/env python3

from time import sleep

from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()
leds = Leds()

print("Press the touch sensor to change the LED color!")
timeout = 0
sequence = ""

while True:
    if ts.is_pressed:
        if timeout == 0:
            leds.set_color("LEFT", "GREEN")
            leds.set_color("RIGHT", "GREEN")
        elif timeout <= 20:
            leds.set_color("LEFT", "YELLOW")
            leds.set_color("RIGHT", "YELLOW")
            sequence += "-"
        timeout += 1
        if timeout <= 20 and timeout < 40:
            
        elif timeout == 40:
            sequence += "."
            timeout = 0
    else:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
        timeout = 0
    print(sequence)
    sleep(0.01)