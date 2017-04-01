''' Thread class to carry data '''
import threading
import os
from cam import capture
from client import Post, PostName

class CaptureThread(threading.Thread):
    ''' DataThread class '''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        loc = capture()
        post = Post(loc)
        pname = PostName(post.response.text)
        print(pname.response.text)
        v = pname.response.text.split(' ')
        self.conn.item = ''.join(v[:len(v) - 1])
        self.conn.accuracy = float(v[len(v) - 1])
        if os.path.exists(loc):
            os.remove(loc)
