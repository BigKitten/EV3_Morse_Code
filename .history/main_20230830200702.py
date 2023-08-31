#!/usr/bin/env python3

import sys
from time import sleep

from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor

ts = TouchSensor()
leds = Leds()

sequence = ""
iterations = 0
timeout = 0


def log(*args, **kwargs):
    return print(*args, **kwargs, file=sys.stderr)


print("[[ READY ]]")


def translate(code):
    valid_chars = {"-", " ", "."}
    if not all(char in valid_chars for char in code):
        raise ValueError("Invalid Morse code character")

    morse_code_dict = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
        "-----": "0",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
    }

    translated = ""
    words = code.split(" ")
    for word in words:
        letters = word.split(" ")
        for letter in letters[:-1]:
            if letter in morse_code_dict:
                translated += morse_code_dict[letter]
            else:
                raise ValueError("Invalid Morse code character: " + letter)
        translated += letters
        translated += " "

    return translated.strip()


def whitespace(sequence):
    if sequence[-6:] == "------":
        sequence = sequence[:-6]
        log("SEQUENCE: " + sequence)
        sequence += " "
        sequence = sequence.lstrip()
        return sequence
    else:
        return sequence


def is_end(sequence):
    if sequence[-10:] == "..........":
        return True
    return False


# ruff-ignore
while True:
    if not is_end(sequence):
        if ts.is_pressed:
            leds.set_color("LEFT", "YELLOW")
            leds.set_color("RIGHT", "YELLOW")
            iterations += 1
        else:
            # if not timeout >= 200:
            if iterations > 0 and iterations <= 20:
                sequence = whitespace(sequence)
                log("ADDED DOT")
                sequence += "."
                leds.set_color("LEFT", "GREEN")
                leds.set_color("RIGHT", "GREEN")
                iterations = 0

            elif iterations > 20:
                sequence = whitespace(sequence)
                log("ADDED DASH")
                sequence += "-"
                leds.set_color("LEFT", "RED")
                leds.set_color("RIGHT", "RED")
                iterations = 0
            else:
                timeout += 1
        # else:
        #     if sequence[-1] != " " and len(sequence) > 0:
        #         sequence += " "
        #     timeout = 0

        if len(sequence) > 0:
            log(translate(sequence))
        sleep(0.01)
    else:
        log("[[ DONE ]]")
        break
