''' Interfaces arduino to raspberrypi '''

from signal_back_thread import SignalBackThread
from capture_thread import CaptureThread
from weighing_scale_interface import WeighingScale
from price import PriceDict

PRICES = PriceDict().price_map
print(PRICES)
MIN_WEIGHT = 50
MAX_WEIGHT = 5000

class Connection:
    ''' Creates and manages connection '''
    def __init__(self):
        self.lastdata = 0
        self.in_session = False
        self.item = ''
        self.accuracy = 0.0
        self.signal_back(text='Welcome!')

    def signal_back(self, data=0, price=0, text='', sleep=0):
        ''' Writes back to serial '''
        if text == '':
            if(abs(self.lastdata-data)>=20):
                self.lastdata=data
            if self.item == '':
                text = '{} gm\r\nProcessing...'.format(data)
            elif self.accuracy < .5:
                text = 'Insufficient\r\naccuracy'
            else:
                text = '{}\r\nRs {}'.format(self.item, price)
        SignalBackThread(text, sleep).start()

    def process(self, data):
        ''' Processes the value obtained from the serial '''
        # Code to multiply with Price comes here
        try:
            d = float(data)
        except ValueError:
            d = 0.0
        if d > MAX_WEIGHT:
            d = 0.0
            print("Over weight")
        print('data = {}'.format(d))
        if d >= MIN_WEIGHT:
            if not self.in_session:
                CaptureThread(self).start()
                self.in_session = True
            else:
                if self.item == '':
                    self.signal_back(d)
                elif self.item in PRICES.keys():
                    self.signal_back(d, PRICES[self.item]*d/1000)
                else:
                    print(self.item)
                    self.signal_back(text="Product not\r\nfound")
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
