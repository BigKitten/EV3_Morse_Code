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

log = lambda *args, **kwargs: print(*args, **kwargs, file=sys.stderr)
log(ts.is_pressed)

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
    log(sequence)
    sleep(0.01)
