''' Thread class to carry data '''
import threading
from cam import capture
from client import Post
import os

class CaptureThread(threading.Thread):
    ''' DataThread class '''
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        loc = capture()
        post = Post(loc)
        self.item = post.response.text
        print(self.item)
        if os.path.exists(loc):
            os.remove(loc)
