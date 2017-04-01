import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)

hx.set_reading_format("LSB", "MSB")

hx.set_reference_unit(92 * 858 / 226)

hx.reset()
hx.tare()

while True:
    try:

        val = hx.get_weight(5)
        print(val)

        hx.power_down()
        hx.power_up()
        time.sleep(0.5)
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
