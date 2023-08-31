#!/usr/bin/env python3

from time import sleep

from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()
leds = Leds()

print("[[ READY ]]")

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

    print(sequence)
    sleep(0.01)
