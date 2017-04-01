import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

class WeighingScale(object):
    def __init__(self):
        self.hx = HX711(5, 6)

        self.hx.set_reading_format("LSB", "MSB")

        self.hx.set_reference_unit(92 * 858 / 226)

        self.hx.reset()
        self.hx.tare()

    def loop(self, fn):
        while True:
            try:
                val = int(self.hx.get_weight(5)[0])
                print(val)
                fn(val)

                self.hx.power_down()
                self.hx.power_up()
                time.sleep(0.5)
            except (KeyboardInterrupt, SystemExit):
                cleanAndExit()
