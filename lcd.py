from RPLCD import CharLCD

def main():
    lcd = CharLCD(rows=2, cols=16)
    lcd.write_string('Hello world')

if __name__ == '__main__':
    main()
