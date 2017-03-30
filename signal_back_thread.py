''' Thread for signalling back '''
import threading
import time

class SignalBackThread(threading.Thread):
    ''' SignalBackThread class '''
    lock = threading.Lock()
    def __init__(self, ser, text, sleep):
        threading.Thread.__init__(self)
        self.text = text
        self.ser = ser
        self.sleep = sleep

    def run(self):
        if self.sleep > 0:
            time.sleep(self.sleep)
        try:
            SignalBackThread.lock.acquire()
            self.ser.write(bytes('<{}>'.format(self.text), 'UTF-8'))
            SignalBackThread.lock.release()
        except TypeError:
            pass
