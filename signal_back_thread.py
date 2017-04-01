''' Thread for signalling back '''
import threading
import time
from lcd import LCD

class SignalBackThread(threading.Thread):
    ''' SignalBackThread class '''
    lock = threading.Lock()
    def __init__(self, text, sleep):
        threading.Thread.__init__(self)
        self.text = text
        self.sleep = sleep

    def run(self):
        if self.sleep > 0:
            time.sleep(self.sleep)
        try:
            SignalBackThread.lock.acquire()
            LCD().write(self.text)
            SignalBackThread.lock.release()
        except TypeError:
            pass
