''' Thread class to carry data '''
import threading
from cam import capture
from client import Post, PostName
import os
import re

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
        self.conn.item = v[0]
        self.conn.accuracy = v[1]
        if os.path.exists(loc):
            os.remove(loc)
