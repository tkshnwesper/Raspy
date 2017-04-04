''' Interfaces arduino to raspberrypi '''
# pylint: disable=C0103

from platform import system
import serial
from signal_back_thread import SignalBackThread
from capture_thread import CaptureThread
from weighing_scale_interface import WeighingScale

SERIAL_ARG = 'COM3' if system() == 'Windows' else '/dev/ttyACM0'
BAUDRATE = 9600

MIN_WEIGHT = 50

class Connection:
    ''' Creates and manages connection '''
    def __init__(self):
        self.in_session = False
        self.item = ''
        self.accuracy = 0.0
        self.signal_back(text='Welcome!')

    def signal_back(self, data=0, price=0, text='', sleep=0):
        ''' Writes back to serial '''
        if text == '':
            if self.item == '':
                text = '{} gm'.format(data) + ' ' * 7 + 'Processing...'
            elif self.accuracy < .5:
                text = 'Insufficient    accuracy'
            else:
                text = '{} {} gm Rs. {}'.format(self.item, data, price)
        SignalBackThread(text, sleep).start()

    def process(self, data):
        ''' Processes the value obtained from the serial '''
        # Code to multiply with Price comes here
        try:
            d = float(data)
        except ValueError:
            d = 0
        print('data = {}'.format(d))
        if d >= MIN_WEIGHT:
            if not self.in_session:
                CaptureThread(self).start()
                self.in_session = True
            else:
                self.signal_back(d, d * 2)
        else:
            if self.in_session:
                print("out of session")
                self.in_session = False
                self.signal_back(text="Welcome!", sleep=2)
                self.item = ''
                self.accuracy = 0.0


    def start(self):
        ''' Starts the Connection '''
        WeighingScale().loop(self.process)

if __name__ == '__main__':
    __con__ = Connection()
    __con__.start()
