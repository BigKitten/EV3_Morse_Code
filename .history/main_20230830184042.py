#!/usr/bin/env python3

from time import sleep

from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()
leds = Leds()

print("Press the touch sensor to change the LED color!")
timeout = 0
sequence = ""

import time

sequence = ""
iterations = 0
timeout = 0

while True:
    if ts.is_pressed:
        iterations += 1
    else:
        if iterations <= 20:
            sequence += "."
        else:
            sequence += "-"
        iterations = 0
        timeout = 0

    timeout += 1
    if timeout > 100:
        leds.set_color("LEFT", "RED")
        leds.set_color("RIGHT", "RED")
        timeout = 0

    print(sequence)
    time.sleep(0.01)