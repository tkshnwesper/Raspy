''' Interfaces arduino to raspberrypi '''
# pylint: disable=C0103

from platform import system
import serial
from signal_back_thread import SignalBackThread
from capture_thread import CaptureThread

SERIAL_ARG = 'COM3' if system() == 'Windows' else '/dev/ttyACM0'
BAUDRATE = 9600

MIN_WEIGHT = 50

class Connection:
    ''' Creates and manages connection '''
    def __init__(self):
        self.ser = serial.Serial(SERIAL_ARG, BAUDRATE, timeout=0)
        self.in_session = False
        self.item = ''

    def signal_back(self, data, price):
        ''' Writes back to serial '''
        # self.ser.write('<{} {} gm Rs. {}>'.format(self.item, data, price))
        SignalBackThread(self.ser, self.item, data, price).start()

    def process(self, data):
        ''' Processes the value obtained from the serial '''
        # Code to multiply with Price comes here
        try:
            d = int(data)
        except ValueError:
            d = 0
        print('data = {}'.format(d))
        if d >= MIN_WEIGHT:
            if not self.in_session:
                CaptureThread().start()
                self.in_session = True
            else:
                self.signal_back(data, data * 2)
        else:
            if self.in_session:
                self.in_session = False

    def start(self):
        ''' Starts the Connection '''
        buffer = []
        while True:
            line = self.ser.readline()
            if len(line) > 0:
                buffer.append(line)
                # print(buffer)
                if b''.join(buffer).endswith(b'\r\n'):
                    val = b''.join(buffer).split(b'\r\n')[0].decode('utf-8')
                    print(val)
                    self.process(val)
                    buffer.clear()

if __name__ == '__main__':
    __con__ = Connection()
    __con__.start()
