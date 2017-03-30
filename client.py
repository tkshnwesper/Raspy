''' Sends the image to server and prints out the response '''
import os
import requests

URL = "http://127.0.0.1:8080/analyse"
FOLDER = "client-image"
# IMAGE_FILE = "banana.jpg"
# FILES = {
#     'img': open(os.path.join(FOLDER, IMAGE_FILE), "rb")
# }

class Post(object):
    ''' Post object '''
    def __init__(self, fname):
        files = {
            'img': open(os.path.join(FOLDER, fname), "rb")
        }
        self.response = requests.post(URL, files=files)
        # print(_response.text)

# if __name__ == "__main__":
#     Post()
