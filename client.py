''' Sends the image to server and prints out the response '''
import requests
from cam import capture

_U = 'http://192.168.43.199'
URL = _U + ":8080/analyse"
IMAGE_SAVE_URL = _U + ':9090'
FOLDER = "client-image"
# IMAGE_FILE = "banana.jpg"
# FILES = {
#     'img': open(os.path.join(FOLDER, IMAGE_FILE), "rb")
# }

class Post(object):
    ''' Post object '''
    def __init__(self, fname):
        files = {
            'img': open(fname, "rb")
        }
        self.response = requests.post(IMAGE_SAVE_URL, files=files)
        print(self.response.text)

class PostName(object):
    ''' Post image name '''
    def __init__(self, imgname):
        self.response = requests.post(URL, data={'imgname': imgname})


if __name__ == "__main__":
    loc = capture()
    post = Post(loc)
    pname = PostName(post.response.text)
    print(pname.response.text)
