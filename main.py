#!/usr/bin/python3
#
# main.py shows vl53l0x tof reading on ht16k33 7-segment display
#

import time

from vl53l0x.api import VL53L0X
from ht16k33.api import HT16K33

if __name__== "__main__":
    tof = VL53L0X()
    led = HT16K33()

    tof.setup()
    led.setup()

    rest = 0.1
    while True:
        distance = tof.measure()
        led.display(distance)
        time.sleep(rest)
