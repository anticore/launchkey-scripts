from time import sleep
from random import randint


def randomcolors(lk, time):
    for led in lk.leds:
        lk.led(led, randint(0, 126))
    sleep(0.5)
