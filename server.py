''' Executes the command '''

import subprocess
import os
import cherrypy

IMAGE_DIRECTORY = "server-image"
DOCKER_COMMAND = "python /tf_files/label_image1.py /tf_files/Raspy/server-image/{}"

class Command(object):
    @cherrypy.expose
    def analyse(self, imgname):
        ''' executes command '''
        result = subprocess.check_output(DOCKER_COMMAND.format(imgname), shell=True)
        ## delete file
        fname = '{}/{}'.format(IMAGE_DIRECTORY, imgname)
        if os.path.exists(fname):
            os.remove(fname)
        return result

if __name__ == "__main__":
    from cherrypy.process import servers
    def fake_wait_for_occupied_port(host, port): return
    servers.wait_for_occupied_port = fake_wait_for_occupied_port
    # cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    config = {
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_timeout' : 60,
            'server.socket_port': 8080
        }
    }
    cherrypy.quickstart(Command(), '/', config)
