from RPLCD import CharLCD

class LCD(object):
    def __init__(self):
        self.lcd = CharLCD(rows=2, cols=16)
    
    def write(self, text):
        self.lcd.write_string(text)
        
