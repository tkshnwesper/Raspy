import requests

URL = "http://127.0.0.1:8080/analyse"
IMAGE_FILE = "banana.jpg"

FILES = {
    'img': open(IMAGE_FILE, "rb")
}

class Post(object):
    def __init__(self):
        r = requests.post(URL, files=FILES)
        print(r.text)

if __name__ == "__main__":
    Post()