import cherrypy
import uuid
import os
import subprocess

IMAGE_DIRECTORY = "image"
DOCKER_COMMAND = "dir"

class Server(object):
    @cherrypy.expose
    def index(self):
        return "Welcome to the FYP Server. POST /analyse [image file] : plain/text"
    
    @cherrypy.expose
    def analyse(self, img):
        imgName = uuid.uuid4().hex
        all_data = bytearray()
        # check if directory exists, if not creates one
        if not os.path.exists(IMAGE_DIRECTORY):
            os.makedirs(IMAGE_DIRECTORY)
        # image will be saved with name IMAGE_DIRECTORY/id
        fname = os.path.join(IMAGE_DIRECTORY, imgName)
        f = open(fname, "wb")
        while True:
            data = img.file.read(8192)
            all_data += data
            if not data:
                break
        # write image data to file
        f.write(all_data)
        f.close()
        # run docker command
        result = subprocess.run(DOCKER_COMMAND, stdout=subprocess.PIPE, shell=True)
        # delete file
        if os.path.exists(fname):
            os.remove(fname)
        return result.stdout

if __name__ == "__main__":
    cherrypy.quickstart(Server())