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
        self.conn.item = pname.response.text[:len(pname.response.text)-4]
        self.conn.accuracy = pname.response.text[len(pname.response.text)-3:]
        if os.path.exists(loc):
            os.remove(loc)
