'''
Module which acts as a server, and processes the requests of clients
'''
import uuid
import os
import subprocess
import cherrypy

IMAGE_DIRECTORY = "server-image"
# DOCKER_COMMAND = "dir"

class Server(object):
    ''' Server class '''
    @cherrypy.expose
    def index(self):
        ''' Serves /index path '''
        return "Welcome to the FYP Server. POST /analyse [image file] : plain/text"

    @cherrypy.expose
    def analyse(self, img):
        ''' Serves /analyse path '''
        imgname = uuid.uuid4().hex + '.jpeg'
        all_data = bytearray()
        # check if directory exists, if not creates one
        if not os.path.exists(IMAGE_DIRECTORY):
            os.makedirs(IMAGE_DIRECTORY)
        # image will be saved with name IMAGE_DIRECTORY/id
        fname = os.path.join(IMAGE_DIRECTORY, imgname)
        _file = open(fname, "wb")
        while True:
            data = img.file.read(8192)
            all_data += data
            if not data:
                break
        # write image data to file
        _file.write(all_data)
        _file.close()
        # run docker command
        # result = subprocess.check_output(DOCKER_COMMAND, shell=True)
        # delete file
        # if os.path.exists(fname):
        #     os.remove(fname)
        return imgname

if __name__ == "__main__":
    from cherrypy.process import servers
    def fake_wait_for_occupied_port(host, port): return
    servers.wait_for_occupied_port = fake_wait_for_occupied_port
    # cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    config = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_timeout' : 60
        }
    }
    cherrypy.quickstart(Server(), '/', config)
