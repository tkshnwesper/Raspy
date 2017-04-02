from RPLCD import CharLCD
from RPi import GPIO

class LCD(object):
    def __init__(self):
        self.lcd = CharLCD(pin_rs=22, pin_rw=24, pin_e=23, pins_data=[9,25,11,8],
        numbering_mode=GPIO.BCM, rows=2, cols=16)
    
    def write(self, text):
        self.lcd.write_string(text)
        
