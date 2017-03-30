''' Thread for signalling back '''
import threading

class SignalBackThread(threading.Thread):
    ''' SignalBackThread class '''
    lock = threading.Lock()
    def __init__(self, ser, text):
        threading.Thread.__init__(self)
        self.text = text
        self.ser = ser

    def run(self):
        try:
            SignalBackThread.lock.acquire()
            self.ser.write(bytes(self.text, 'UTF-8'))
            SignalBackThread.lock.release()
        except TypeError:
            pass
