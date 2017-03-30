''' Thread for signalling back '''
import threading

class SignalBackThread(threading.Thread):
    ''' SignalBackThread class '''
    lock = threading.Lock()
    def __init__(self, ser, item, data, price):
        threading.Thread.__init__(self)
        self.data = data
        self.price = price
        self.item = item
        self.ser = ser

    def run(self):
        try:
            SignalBackThread.lock.acquire()
            self.ser.write(bytes('<{} {} gm Rs. {}>'.format(self.item, self.data, self.price), 'UTF-8'))
            SignalBackThread.lock.release()
        except TypeError:
            pass
