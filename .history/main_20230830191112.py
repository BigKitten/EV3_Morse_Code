#!/usr/bin/env python3

import sys
from time import sleep

from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()
leds = Leds()

print("[[ READY ]]")

sequence = ""
iterations = 0
timeout = 0


def log(*args, **kwargs):
    return print(*args, **kwargs, file=sys.stderr)


log(ts.is_pressed)

print("[[ READY ]]")

while True:
    if ts.is_pressed:
        leds.set_color("LEFT", "YELLOW")
        leds.set_color("RIGHT", "YELLOW")
        iterations += 1
    else:
        if not timeout >= 200:
            if iterations > 0 and iterations <= 20:
                log("ADDED DOT")
                sequence += "."
                leds.set_color("LEFT", "GREEN")
                leds.set_color("RIGHT", "GREEN")
                iterations = 0
            elif iterations > 20:
                log("ADDED DASH")
                sequence += "-"
                leds.set_color("LEFT", "RED")
                leds.set_color("RIGHT", "RED")
                iterations = 0
            else:
                timeout += 1
        else:
            sequence += " "

    print(sequence)
    log(sequence)
    sleep(0.01)