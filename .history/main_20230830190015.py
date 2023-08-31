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

print("[[ START ]]")

while True:
    if ts.is_pressed:
        iterations += 1
    else:
        log("ELSE")
        log(iterations)
        if iterations > 0 <= 20:
            log("ADDED DOT")
            sequence += "."
            iterations = 0
        elif iterations > 20:
            log("ADDED DOT")
            sequence += "-"
            iterations = 0

    print(sequence)
    log(sequence)
    sleep(0.01)